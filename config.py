VA_NAME = 'ATOM Connect'

VA_VER = '1.5'

VA_ALIAS = ('атом', 'а томик', 'а томчик', 'машина', 'авто', 'автомобиль', 'а там', 'о том', 'адам', 'от он', 'атон', 'а тон')

VA_TBR = ('включи', 'подключи', 'выключи', 'отключи',
          'открой', 'отопри', 'закрой', 'запри',
          'убавь', 'прибавь', 'сложи', 'разложи',
          'заведи', 'заглуши')

VA_ATOM_CMDS = {
    'hi': ('привет', 'здарова', 'ку'),
    'bye': ('пока', 'прощай', 'до свидания', 'до следующей поездки', 'до встречи'),
    'dela': ('как дела', 'как твои дела', 'как прошёл твой день', 'как настроение'),
    'current_time': ('время', 'текущее время', 'сейчас времени', 'который час', 'сколько времени'),
    'joke': ('расскажи шутку', 'расскажи анекдот', 'шутка', 'анекдот', 'скажи шутку', 'скажи анекдот'),
    'change_windows': ('подогрев окон', 'подогрей окна', 'согрей окна', 'подогрев всех стекол', 'подогрей все окна', 'согрей все окна', 'окна'),
    'change_mirrors': ('боковые зеркала', 'зеркала заднего вида', 'зеркала', 'оба зеркала'),
    'set_backlight': ('поменяй цвет подсветки', 'поменяй подсветку', 'измени подсветку', 'хочу другую подсветку'),
    'seat_forward': ('подвинь сидение вперёд', 'подвинь кресло вперёд', 'сделай кресло ближе к рулю', 'кресло вперёд', 'подвинь сидение вперёд'),
    'seat_backward': ('подвинь сидение назад', 'подвинь кресло назад', 'кресло назад', 'отодвинь кресло', 'сидение назад', 'отодвинь сидение'),
    'chair_forward': ('подвинь спинку кресла вперед', 'подвинь спинку сидения вперед', 'подними спинку кресла', 'подними спинку сидения', 'спинку кресла ближе к рулю', 'сделай спинку кресла ближе к рулю', 'сделай спинку сидения ближе к рулю'),
    'chair_backward': ('подвинь спинку кресла назад', 'опусти спинку кресла', 'опусти спинку сидения', 'спинку кресла назад', 'спинку сидения назад', 'сделай спинку назад', 'подвинь спинку сидения назад'),
    'change_music': ('музыку', 'хочу музыку'),
    'change_trunk': ('багажник', 'багажник электромобиля'),
    'change_hood': ('капот', 'капот электромобиля'),
    'change_headlights': ('фары', 'фары', 'свет'),
    'change_heating': ('подогрев сидений', 'подогрев кресел', 'подогрей кресла', 'согрей кресла', 'согрей сидения'),
    'change_car': ('машину', 'двери', 'электромобиль'),
    'change_thermoregulation': ('терморегуляцию', 'климат контроль')
}

VA_ATOM_ANSWERS = {
    'change_windows': 'Включаю подогрев окон, теперь хорошо видно?',
    '!change_windows': 'Выключаю подогрев окон, надеюсь они распотели',
    'change_mirrors': 'Складываю боковые зеркала, чтобы вы никого не задели',
    '!change_mirrors': 'Раскладываю боковые зеркала, чтобы вы всё видели',
    'set_backlight': 'Меняю цвет подсветки, на более комфортный',
    'seat_forward': 'Двигаю сидения вперёд, аккуратно, не прищемите свои ноги',
    'seat_backward': 'Двигаю сидения назад, не придавите никого!',
    'chair_forward': 'Двигаю спинку кресла вперёд, не жмет?',
    'chair_backward': 'Двигаю спинку кресла назад, располагайтесь как удобно',
    'change_music': 'Включаю музыку. Будет громко?',
    '!change_music': 'Выключаю музыку, теперь будет тихо',
    'change_trunk': 'Открываю багажник, даа',
    '!change_trunk': 'Закрываю багажник, ничего не забыли положить?)',
    'change_hood': 'Открываю капот, берите вещи',
    '!change_hood': 'Закрываю капот, уберите пальцы из под крышки капота._.',
    'change_headlights': 'Включаю фары, чтобы осветить все вокруг',
    '!change_headlights': 'Выключаю фары, чтобы стало темно',
    'change_seat_heating': 'Включаю подогрев сидений для вашей попы',
    '!change_seat_heating': 'Выключаю подогрев сидений, надеюсь вы согрелись',
    'change_car': 'Открываю машину специально для вас',
    '!change_car': 'Закрываю машину, чтобы ничего не украли-_-',
    'change_thermoregulation': 'Включаю климат контроль, будет тепло...',
    '!change_thermoregulation': 'Выключаю климат контроль, осторожно!'
}

VA_METHODS_TO_ATTRS = {
    'change_mirrors': 'mirrors_folded',
    'change_windows': 'windows_heated',
    'change_music': 'music_on',
    'change_trunk': 'trunk_open',
    'change_hood': 'hood_open',
    'change_headlights': 'headlights_on',
    'change_seat_heating': 'seats_heated',
    'change_car': 'car_open',
    'change_thermoregulation': 'thermoregulation_on'
}

JOKES = (
    'Сын сказал, что когда вырастет, у него будет\nнесколько профессий: клоун, фокусник и программист.\nОн ещё не знает, что в IT это одна профессия.',
    'Чем программист-экстроверт отличается от\nпрограммиста-интроверта? Экстроверт во время собеседования\nсмотрит на твои шнурки, а интроверт - на свои',
    'Молодой хакер спрашивает у более опытного -\nскажи, а как ты зарабатываешь в интернете? Ну тот такой\nпомялся и говорит - перечисли мне на счет\n100 рублей, скажу. Ну тот перечислил. Ну, говорит,\nскажи как. - Ну как как, говорит, вот так и зарабатываю.',
    'Попроси программиста проверить десять строк\nкода, он найдёт десять проблем. Попроси его проверить\nпятьсот строк, он скажет, что выглядит норм.',
    'Программист - это единственная в мире профессия,\nгде платят деньги, чтобы ты исправил ошибки,\nкоторые допустил, когда перед этим сделал\nсвою работу херово.',
    'Бог по ошибке выпустил приложение "две тысячи\nдвадцатый год" с вирусом. Исправление две тысячи\nдвадцать первого не помогло. Как бы ему\nне пришлось переустанавливать систему?',
    'Я программист простой: если задача простая,\nто мне скучно, а если сложная — трудно и страшно,\nчто не получится сделать.',
    'Сольфеджио для программистов: интервьюер\nчитает тебе вслух код, а ты должен сказать,\nчто этот код делает.',
    'Зачем к устройству с "интуитивно-понятным\nинтерфейсом" инструкция на сто плюс страниц?',
    'Любая курица легко может программировать,\nесли на клавиатуру насыпать зерно.',
    'Когда появятся беспилотные самолеты,\nпервыми в них откажутся летать программисты.'
)
