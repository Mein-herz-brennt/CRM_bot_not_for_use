from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from crm_state import CRM_state
import asyncio
import json
import os

# link: t.me/nice_crm_bot

storage = MemoryStorage()
loop = asyncio.get_event_loop()
bot = Bot(token='2076970810:AAHMRY45yaAdO4mbbcn2tcge-Q0ZOjmS4pk', parse_mode='html')
dp = Dispatcher(bot, loop=loop, storage=storage)
info = {"CRM": []}


# user_info = {"first_name": "",
#              "phone_number": "",
#              "user_id": ""}


def reader():
    with open("215037238.json", "r") as file:
        inf = json.load(file)
    return inf


def adder(inf):
    with open("215037238.json", "w") as file:
        json.dump(inf, file, indent=3)


def creator_info():
    with open("215037238.json", "w") as file:
        information = {"objects": [],
                       "details": {"Privat": " ",
                                   "Mono": " ",
                                   "Phone_number": " "},
                       "clients": [],
                       "Reports": []
                       }
        info["CRM"].append(information)
        json.dump(info, file, indent=3)


def check_id(__id):
    inf = reader()
    for i in inf["CRM"][0]["clients"]:
        if str(__id) == i["user_id"]:
            return True
    else:
        return False


def add_details(add, more, number=0):
    inf = reader()
    if more.lower() == "mono":
        if add == "add":
            inf['CRM'][0]['details']['Mono'] = number
        elif add == "dell":
            inf['CRM'][0]['details']['Mono'] = " "
    elif more.lower() == "privat":
        if add == "add":
            inf["CRM"][0]["details"]["Privat"] = number
        elif add == "dell":
            inf["CRM"][0]["details"]["Privat"] = " "
    if more.lower() == "phone":
        if add == "add":
            inf["CRM"][0]["details"]["Phone_number"] = number
        elif add == "dell":
            inf["CRM"][0]["details"]["Phone_number"] = " "
    adder(inf)


def add_clients(add, client_info):
    inf = reader()
    if add == "add":
        inf["CRM"][0]["clients"].append(client_info)
    elif add == "dell":
        for i in range(len(inf["CRM"][0]["clients"])):
            if inf["CRM"][0]["clients"][i]["first_name"] == client_info["first_name"]:
                inf["CRM"][0]["clients"].pop(i)
    adder(inf)


def add_objects(add, object_name):
    inf = reader()
    if add == "add":
        inf["CRM"][0]["objects"].append(object_name)
    elif add == "dell":
        for i in range(len(inf["CRM"][0]["objects"])):
            if inf["CRM"][0]["objects"][i] == object_name:
                del inf["CRM"][0]["objects"][i]
    adder(inf)


def get_debt(user_id):
    inf = reader()
    for i in inf["CRM"][0]["clients"]:
        if user_id == i["user_id"]:
            if len(i["debt"]) > 0:
                return str(i["debt"])
            else:
                return 0
    else:
        return 0


def add_debt(user_id, debt_num):
    inf = reader()
    for i in inf["CRM"][0]["clients"]:
        if str(user_id) == i['user_id']:
            i["debt"] = debt_num
            break
    adder(inf)


def add_adres(user_id, adres):
    inf = reader()
    for i in inf["CRM"][0]["clients"]:
        if str(user_id) == i['user_id']:
            i["adres"] = adres
            break
    adder(inf)


keyboard_user = types.ReplyKeyboardMarkup(resize_keyboard=True)
debt_button = types.KeyboardButton(text="Мої борги")
bank_button = types.KeyboardButton(text="Переглянути реквізити власника")
photo_button = types.KeyboardButton(text="Надіслати фото чеку")
keyboard_user.add(debt_button).add(bank_button).add(photo_button)

keyboard_contact = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
button_contact = types.KeyboardButton(text="Можна ваш контакт?", request_contact=True)
keyboard_contact.add(button_contact)

start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
pay_button = types.KeyboardButton(text='Нагадати про оплату')
path_pay_button = types.KeyboardButton(text='Перевірити борги')
settings_button = types.KeyboardButton(text='Налаштування')
start_keyboard.add(pay_button).add(path_pay_button).add(settings_button)

settings_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
change_button = types.KeyboardButton(text='Змінити реквізити💳')
objects_button = types.KeyboardButton(text="Мої об'єкти")
delete_button = types.KeyboardButton(text='Мої орендарі')
back_button = types.KeyboardButton(text='Назад')
settings_keyboard.add(objects_button).add(delete_button).add(change_button).add(back_button)

add_objects_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
add_button = types.KeyboardButton(text="Додати об'єкт")
dell_button = types.KeyboardButton(text="Видалити об'єкт")
come_back_button = types.KeyboardButton(text="Назад")
add_objects_keyboard.add(add_button).add(dell_button).add(come_back_button)

details_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
b_button = types.KeyboardButton(text="Мої карти")
phone_button = types.KeyboardButton(text="Телефон")
back_button = types.KeyboardButton(text='Назад')
details_keyboard.add(b_button).add(phone_button).add(back_button)

bank_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
add_button = types.KeyboardButton(text="Додати карту")
dell_button = types.KeyboardButton(text="Видалити карту")
back_button = types.KeyboardButton(text="Назад")
bank_keyboard.add(add_button).add(dell_button).add(back_button)

orenda_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
orendar = types.KeyboardButton(text="Переглянути інформацію по орендарях")
dell_orendar = types.KeyboardButton(text="Видалити орендаря")
back_button = types.KeyboardButton(text='Назад')
orenda_keyboard.add(orendar).add(dell_orendar).add(back_button)


@dp.message_handler(commands=["start"])
async def command_start(message: types.Message):
    id_ = message.from_user.id
    if id_ == 789402487:  # or 789402487 830944177 215037238
        await message.answer("Вітаю господар", reply_markup=start_keyboard)
    else:
        await message.answer("Вітаю незнайомець", reply_markup=keyboard_contact)


@dp.message_handler(content_types=["contact"])
async def contact_command(message: types.Message):
    global vyl, info, user_info, id_
    id_ = message.from_user.id
    # contact = message.contact
    danetka = types.InlineKeyboardMarkup()
    yeas_b = types.InlineKeyboardButton(text="так", callback_data="так")
    no_b = types.InlineKeyboardButton(text="ні", callback_data="ні")
    danetka.add(yeas_b, no_b)
    user_info = {
        'first_name': f"{message.contact.first_name}",
        'phone_number': f"{message.contact.phone_number}",
        'user_id': f"{message.contact.user_id}",
        'debt': "",
        'adres': "",
    }
    # add_clients("add", user_info)
    await message.forward(789402487)  # 789402487 215037238
    await bot.send_message(789402487, "Підтвердити користувача?", reply_markup=danetka)


@dp.callback_query_handler(text="так")
async def yeas_danetka(call: types.CallbackQuery):
    global id_, user_info
    add_clients("add", user_info)
    await bot.send_message(id_, "Вас додано до списку орендарів", reply_markup=keyboard_user)
    await bot.answer_callback_query(call.id, "Орендаря успішно додано!")
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    await call.message.answer("Введіть ціну оренди для цього користувача")
    await CRM_state.debt.set()


@dp.message_handler(state=CRM_state.debt)
async def cent_debt(message: types.Message):
    global id_
    add_debt(id_, message.text)
    await message.answer("Ціну оренди встановлено")
    await message.answer("Введіть назву об'єкту який буде закріплено за цим користувачем")
    await CRM_state.obj.set()


@dp.message_handler(state=CRM_state.obj)
async def add_obj_to_user(message: types.Message, state: FSMContext):
    global id_
    add_adres(id_, message.text)
    await message.answer("Об'єкт закріплено за користувачем", reply_markup=start_keyboard)
    await state.finish()


@dp.callback_query_handler(text="ні")
async def no_danetka(call: types.CallbackQuery):
    global id_
    await bot.send_message(id_, "Вибачте та ви не один з орендарів")
    await bot.answer_callback_query(call.id, "Орендаря не додано!")
    await bot.delete_message(call.message.chat.id, call.message.message_id)

    # with open("nice.json", "w") as f:
    #     info["data"].append(a)
    #     json.dump(info, f, indent=3)


@dp.message_handler(text="Перевірити борги")
async def check_debts(message: types.Message):
    await message.answer("Відправка чеків почалась")
    for files in os.listdir("photos"):
        file = types.InputFile(rf"photos\{files}", files)
        await message.answer_document(file)
    await message.answer("Відправка чеків закінчилась")


@dp.message_handler(text="Налаштування")
async def settings(message: types.Message):
    await message.answer("Ви в розділі налаштувань", reply_markup=settings_keyboard)


@dp.message_handler(text="Назад")
async def back(message: types.Message):
    await message.answer("Ви повернулись до головного меню", reply_markup=start_keyboard)


@dp.message_handler(text="Мої об'єкти")
async def my_objects(message: types.Message):
    await message.answer("Ви в меню об'єктів", reply_markup=add_objects_keyboard)


@dp.message_handler(text=["Додати об'єкт", "Видалити об'єкт"])
async def object_command(message: types.Message):
    global adde
    if message.from_user.id == 789402487:
        if message.text == "Додати об'єкт":
            adde = True
            await message.answer("Очікую назву об'єкту")
            await CRM_state.object1.set()
        else:
            adde = False
            await message.answer("Очікую назву об'єкту")
            await CRM_state.object1.set()
    else:
        await message.answer("Ви не можете додавати об'єкти")


@dp.message_handler(state=CRM_state.object1)
async def add(message: types.Message, state: FSMContext):
    global adde
    objec = message.text
    if adde:
        add_objects("add", objec)
        await message.answer("Новий об'єкт додано", reply_markup=start_keyboard)
        await state.finish()
    elif not adde:
        add_objects("dell", objec)
        await message.answer("Об'єкт видалено", reply_markup=start_keyboard)
        await state.finish()


@dp.message_handler(text="Змінити реквізити💳")
async def details(message: types.Message):
    await message.answer("Ви в меню реквізитів, тут можна додати чи видалити вашу карту чи номер телефону",
                         reply_markup=details_keyboard)


@dp.message_handler(text="Телефон")
async def phone_number(message: types.Message):
    phone_keyb = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    phone_add = types.KeyboardButton(text="Додати номер телефону")
    phone_dell = types.KeyboardButton(text="Видалити номер телефону")
    back_but = types.KeyboardButton(text="Назад")
    phone_keyb.add(phone_add).add(phone_dell).add(back_but)
    await message.answer("Виберіть дію", reply_markup=phone_keyb)
    await CRM_state.phone.set()


@dp.message_handler(state=CRM_state.phone)
async def phoner(message: types.Message, state: FSMContext):
    text = message.text
    if text == "Додати номер телефону":
        await message.answer("Введіть номер телефону"
                             "Він має починатись на +380")
        await CRM_state.phone_adder.set()
    elif text == "Видалити номер телефону":
        add_details("dell", "phone")
        await message.answer("Номер видалено", reply_markup=settings_keyboard)
        await state.finish()
    else:
        await message.answer("ви повернулись до меню деталей", reply_markup=settings_keyboard)
        await state.finish()


@dp.message_handler(state=CRM_state.phone_adder)
async def phone_adder(message: types.Message, state: FSMContext):
    text = message.text
    if text.startswith("+380") and len(text) == 13:
        add_details("add", "phone", number=text)
        await message.answer("телефон додано", reply_markup=settings_keyboard)
        await state.finish()


@dp.message_handler(text=["Мої карти"])
async def privat(message: types.Message):
    await message.answer("Виберіть дію", reply_markup=bank_keyboard)
    await CRM_state.bank1_1.set()


@dp.message_handler(state=CRM_state.bank1_1)
async def card_adder1(message: types.Message, state: FSMContext):
    text = message.text
    if text == "Додати карту":
        inl_keyb_b = types.InlineKeyboardMarkup()
        priv_but = types.InlineKeyboardButton(text="Privat", callback_data="privat1")
        mono_but = types.InlineKeyboardButton(text="Mono", callback_data="mono1")
        inl_keyb_b.add(priv_but, mono_but)
        await message.answer("Виберіть карту якого банку ви хочете додати", reply_markup=inl_keyb_b)
        await state.finish()
    elif text == "Видалити карту":
        await state.finish()
        keyb_dell = types.InlineKeyboardMarkup()
        keyb_button_p = types.InlineKeyboardButton(text="Privat", callback_data="Privat")
        keyb_button_m = types.InlineKeyboardButton(text="Mono", callback_data="Mono")
        keyb_dell.add(keyb_button_p).add(keyb_button_m)
        await message.answer("Виберіть карту яку хочете видалити", reply_markup=keyb_dell)
    elif text == "Назад":
        await message.answer("Ви повернулися до головного меню", reply_markup=start_keyboard)
        await state.finish()


@dp.message_handler(state=CRM_state.bank1_2)
async def add_privat(message: types.Message):
    numb = message.text
    if len(numb) == 16:
        add_details("add", "privat", number=numb)
        await message.answer(f"Карту: {numb}\n"
                             f"Банк: Privat\n"
                             f"Додано!!!")
        await CRM_state.bank1_1.set()
    else:
        await message.answer("Невірно введений номер карти ,\n"
                             "Будь ласка Спробуйте ще раз!", reply_markup=bank_keyboard)
        await CRM_state.bank1_1.set()


@dp.message_handler(state=CRM_state.bank1_3)
async def add_mono(message: types.Message):
    numb = message.text
    if len(numb) == 16:
        add_details("add", "mono", number=numb)
        await message.answer(f"Карту: {numb}\n"
                             f"Банк: Mono\n"
                             f"Додано!!!")
        await CRM_state.bank1_1.set()
    else:
        await message.answer("Невірно введений номер карти ,\n"
                             "Будь ласка Спробуйте ще раз!", reply_markup=bank_keyboard)
        await CRM_state.bank1_1.set()


@dp.callback_query_handler(text="privat1")
async def privat_delete(call: types.CallbackQuery):
    await call.message.answer("Введіть номер карти")
    await CRM_state.bank1_2.set()


@dp.callback_query_handler(text="mono1")
async def privat_delete(call: types.CallbackQuery):
    await call.message.answer("Введіть номер карти")
    await CRM_state.bank1_3.set()


@dp.callback_query_handler(text="Privat")
async def privat_delete(call: types.CallbackQuery):
    add_details("dell", "privat")
    await bot.answer_callback_query(call.id, "Карту успішно видалено")
    await CRM_state.bank1_1.set()
    # await call.message.answer("Ви в меню налаштувань", reply_markup=settings_keyboard)


@dp.callback_query_handler(text="Mono")
async def mono_delete(call: types.CallbackQuery):
    add_details("dell", "mono")
    await bot.answer_callback_query(call.id, "Карту успішно видалено")
    await CRM_state.bank1_1.set()
    # await call.message.answer("Ви повернулися в меню налаштувань", reply_markup=settings_keyboard)


@dp.message_handler(text="Мої орендарі")
async def my_orendars(message: types.Message):
    await message.answer("Виберіть дію", reply_markup=orenda_keyboard)


@dp.message_handler(text="Переглянути інформацію по орендарях")
async def info_users(message: types.Message):
    inf = reader()
    if len(inf["CRM"][0]["clients"]) == 0:
        await message.answer("У вас покищо немає орендарів", reply_markup=settings_keyboard)
    else:
        for i in inf["CRM"][0]["clients"]:
            name = i["first_name"]
            phone = i["phone_number"]
            await message.answer(f"Ім'я:{name}\n"
                                 f"Телефон:{phone}")


@dp.message_handler(text="Видалити орендаря")
async def dell_client(message: types.Message):
    inf = reader()
    ret = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    ret_button = types.KeyboardButton(text="Відмінити")
    ret.add(ret_button)
    for i in inf["CRM"][0]["clients"]:
        name = i["first_name"]
        phone = i["phone_number"]
        await message.answer(f"Ім'я: {name}\n"
                             f"Телефон: {phone}")
    await message.answer("Надішліть ім'я орендаря якого хочете видалити", reply_markup=ret)
    await CRM_state.client_dell.set()


@dp.message_handler(state=CRM_state.client_dell)
async def client_deleter(message: types.Message, state: FSMContext):
    if message.text != "Відмінити":
        inf = reader()
        for i in inf["CRM"][0]["clients"]:
            if i["first_name"] == message.text:
                add_clients("dell", i)
                await message.answer("Орендаря видалено", reply_markup=settings_keyboard)
                await state.finish()
    else:
        await state.finish()
        await message.answer("Ви повернулись у налаштування", reply_markup=settings_keyboard)


@dp.message_handler(text="Нагадати про оплату")
async def remember(message: types.Message):
    rememb_k = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    rem_all = types.KeyboardButton(text="Нагадати всім")
    rem_one = types.KeyboardButton(text="Нагадати одному")
    back = types.KeyboardButton(text="Назад")
    rememb_k.add(rem_one).add(rem_all).add(back)
    await message.answer("Виберіть дію", reply_markup=rememb_k)


@dp.message_handler(text="Нагадати всім")
async def rememb_all(message: types.Message):
    inf = reader()
    if len(inf["CRM"][0]["clients"]) > 0:
        for i in inf["CRM"][0]["clients"]:
            await bot.send_message(i["user_id"], "Настав час внести оплату")
        await message.answer("Орендаря повідомлено", reply_markup=start_keyboard)
    else:
        await message.answer("У вас поки немає орендарів!")


@dp.message_handler(text="Нагадати одному")
async def rememb_one(message: types.Message):
    inf = reader()
    ret = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    ret_button = types.KeyboardButton(text="Відмінити")
    ret.add(ret_button)
    if len(inf["CRM"][0]["clients"]) > 0:
        for i in inf["CRM"][0]["clients"]:
            name = i["first_name"]
            phone = i["phone_number"]
            await message.answer(f"Ім'я: {name}\n"
                                 f"Телефон: {phone}")
        await message.answer("Надішліть номер телефону орендаря якого хочете повідомити", reply_markup=ret)
        await CRM_state.remind.set()
    else:
        await message.answer("У вас поки немає орендарів!")


@dp.message_handler(state=CRM_state.remind)
async def rem(message: types.Message, state: FSMContext):
    await state.finish()
    if message.text != "Відмінити":
        inf = reader()
        for i in inf["CRM"][0]["clients"]:
            if i["phone_number"] == message.text:
                _id = i["user_id"]
                await bot.send_message(_id, "Настав час внести оплату")
        await message.answer("Орендаря повідомлено", reply_markup=start_keyboard)
    else:
        await message.answer("Ви повернулись у головне меню", reply_markup=start_keyboard)


@dp.message_handler(text="Мої борги")
async def user_debt(message: types.Message):
    if check_id(message.from_user.id):
        debt = get_debt(str(message.from_user.id))
        await message.answer(f"Ось ваш борг: {debt}")
    else:
        await message.answer("Ви не є орендарем!!!")


@dp.message_handler(text="Переглянути реквізити власника")
async def user_check_credit(message: types.Message):
    if check_id(message.from_user.id):
        inf = reader()
        privat = inf["CRM"][0]["details"]["Privat"]
        mono = inf["CRM"][0]["details"]["Mono"]
        phone = inf["CRM"][0]["details"]["Phone_number"]
        await message.answer(f"privat: {privat}")
        await message.answer(f"mono: {mono}")
        await message.answer(f"Номер телефону власника: {phone}")
    else:
        await message.answer("Ви не є орендарем!!!")


@dp.message_handler(text="Надіслати фото чеку")
async def check_fun(message: types.Message):
    await message.answer("Будь ласка надішліть фото чеку про оплату")


@dp.message_handler(content_types=["photo"])
async def photo_sender(message: types.Message):
    await message.photo[-1].download()
    await message.forward(789402487)
    await message.answer("Чек відправлено!")
    add_debt(message.from_user.id, 0)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
