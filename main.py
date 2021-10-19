import TelegramModel as tm
import DataModel as dm




if __name__ == '__main__':
    tm = tm.TelegramModel()
    tm.get_userupdate()

    dm = dm.DataModel()
    text = dm.gen_message()

    tm.send_message(text)

