# Case #3
# Developers: Khramchikhina A., Peshkov Y., Sanzhanova A., Yurshenaite A.

import ru_local as ru


def age(year):
    '''
    The function outputs the age if it is greater than or equal to 18.
    '''
    return year >= 18


def beer():
    '''
    The function determines the cost of the selected drink.
    :param type_1, type_2: the selected variety and the name of the drink
    :return: the price of the drink
    '''
    print(ru.LIGHT, ru.DARK, ru.AUTHOR, sep='\n')
    type_1 = int(input(ru.TYPE_1))
    price = 0
    if type_1 == 1:
        print(ru.CORNELLISSEN, ru.LEFFE_BLONDE, ru.LA_GUILLOTINE, ru.HELLEKAPELLE, ru.PETRUS_BLOND, sep='\n')
        type_2 = int(input(ru.TYPE_2))
        match type_2:
            case 1:
                price = 440
            case 2:
                price = 340
            case 3:
                price = 440
            case 4:
                price = 460
            case 5:
                price = 590
    elif type_1 == 2:
        print(ru.LEFFE_BRUNE, ru.DOUBLE_BIE, ru.ZATTE_BIE, ru.CUVEE_CLARISSE, ru.BRUEGEL, sep='\n')
        type_2 = int(input(ru.TYPE_2))
        match type_2:
            case 1:
                price = 340
            case 2:
                price = 390
            case 3:
                price = 440
            case 4:
                price = 490
            case 5:
                price = 350
    else:
        print(ru.ROLLING_WAVES, ru.MAIN_ROAD, ru.CLEAR_SKY, ru.BIG_ROCK, ru.DARK_ISLAND, ru.HIGH_GRASS, sep='\n')
        type_2 = int(input(ru.TYPE_2))
        match type_2:
            case 1:
                price = 300
            case 2:
                price = 290
            case 3:
                price = 300
            case 4:
                price = 300
            case 5:
                price = 350
            case 6:
                price = 340
    return price


def discounts(price_1):
    '''
    The function applies the cost with or without a discount.
    :param discount: availability of a discount card
    :return: the total amount of the purchase
    '''
    discount = input(ru.DISCOUNT).lower()
    price_2 = 0.9*price_1 if discount == ru.YES else price_1
    return price_2


def rubles(price_3):
    '''
    The function gives declines the word "ruble" according to the numeral.
    :param price_3: number of rubles
    :return: the decline of the ruble
    '''
    if 2 <= price_3 % 10 <= 4 and not (11 <= price_3 % 100 <= 14):
        ruble = ru.RUBLE_1
    elif price_3 % 10 == 1 and not (price_3 % 100 == 11):
        ruble = ru.RUBLE_2
    else:
        ruble = ru.RUBLE_3
    return ruble


def main():
    '''
    Main function.
    :return: None
    '''
    years = int(input(ru.AGE))
    if age(years):
        final_price = discounts(beer())
        print(f'{ru.FROM_YOU} {int(final_price)} {rubles(final_price)}.')
    else:
        print(ru.FORBIDDEN)


if __name__ == '__main__':
    main()