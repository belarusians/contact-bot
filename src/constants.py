from enum import Enum, EnumMeta


class MetaEnum(EnumMeta):
    def __contains__(cls, item):
        try:
            cls(item)
        except ValueError:
            return False
        return True


class BaseEnum(Enum, metaclass=MetaEnum):
    pass


class Button(str, BaseEnum):
    REFUGEE_TO_BTN = "Я бежанец"
    IDEAS_TO_BTN = "Ідэі і прапановы"
    OTHER_TO_BTN = "Іншае"

    ADVOCATE_TO_BTN = "Дапамога з адвакатам"
    FINANCE_TO_BTN = "Фінансавая дапамога"
    STUFF_TO_BTN = "Матэрыяльная дапамога"

    ADVOCATE_OTHER_REASONS_BTN = "Іншыя прычыны"
    ADVOCATE_POLITICAL_REASONS_BTN = "Палітычныя прычыны"
    ADVOCATE_HUMANITARIAN_REASONS_BTN = "Гуманітарныя прычыны"

    FINANCE_ADVOCATE_REASONS_BTN = "На адваката"
    FINANCE_ANY_REASONS_BTN = "Хутка любыя патрэбы"

    STUFF_CLOTHES_YS_BTN = "Адзенне для сябе"
    STUFF_CLOTHES_CHILD_BTN = "Адзенне для дзяцей"
    STUFF_CLOTHES_FAMILY_BTN = "Адзенне для сям'і"

    IDEAS_READY_BTN = "Гатова"

    OTHER_READY_BTN = "Гатова"

    CONTACTS_BTN = "Даць кантакт"
    CONTACTS_REJ_BTN = "Адмовіць"


class State(str, BaseEnum):
    REFUGEE_STATE = "refugee"
    IDEAS_STATE = "ideas"
    OTHER_STATE = "other"
    ADVOCATE_STATE = "help-with-advocate"
    FINANCE_STATE = "help-with-finance"
    STUFF_STATE = "help-with-stuff"
    CONTACT_STATE = "contact"
