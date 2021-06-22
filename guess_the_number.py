import random
import time
import os

#region Functions


def terminal_clean():
    '''İşletim sistemine göre terminaldeki ekranı temizler'''
    if os.name == 'nt':
        os.system('cls')   # Terminal ekranını temizler (Windows için)
    elif os.name == 'posix':
        os.system('clear')  # Terminal ekranını temizler (Linux için)


def generate_rules(ilk, son):
    '''Başlangıç sınırı ve bitiş sınırı belli olup ona göre rastgele bir sayı üretip döndürür'''
    return random.randint(ilk, son) # random.randint(min,max) - Max değer dahildir


def game(start=0, finish=100, max_count=10):

    tutulan_sayi = generate_rules(start, finish)
    flag = False
    ilk, son = start, finish
    i = 1
    sayi = -1
    # print("Tutulan sayı : %i"%tutulan_sayi) # --> Tutulan sayıyı baştan görmek istiyor
    while i <= max_count:

        print("%i/%i attempts [ %i - %i ] : " % (i, max_count, ilk, son), end='')
        try:
            sayi = int(input())
        except ValueError:
            pass
        except UnboundLocalError:
            pass
        if tutulan_sayi > sayi and ilk < sayi:
            ilk = sayi
        elif tutulan_sayi < sayi and son > sayi:
            son = sayi
        elif tutulan_sayi == sayi:
            flag = True
            break

        if ilk <= sayi <= son:     # Bu aralıkta ise oyun çalışır öbür türlü çalışmaz
            i += 1
        terminal_clean()                # Her işlemden sonra terminali temizle

    terminal_clean()
    if flag:
        print("You have found the number on your %i. attempt!" % i, "The number was %i" % tutulan_sayi, sep="\n")
    else:
        print("You didn't guess the number : %i" % (tutulan_sayi), sep="\n")


def default_game_menu(answer):
    '''Varsayılan oyun ayarları ile oynanılacak mı oynanılmayacak mı kontrol metodu'''

    # Kabul görülen girişlerin listesi
    # Stringlerin içi eğer boş ise False, dolu ise True value değerleri döndürürler
    # ÖRNEK :
    # string_ex = ""    -->     False
    # string_ex = "5"   -->     True
    check_list = {"Y", "y", "N", "n", ""}

    try:
        assert type(answer) == str
    except AssertionError:
        return False
    else:
        if answer in check_list:
            return True
        else:
            return False

#endregion


if __name__ == "__main__":

    question = "Start? [y/n] "
    is_game_finished = False
    continue_question = False
    terminal_clean()

    while True:

        if continue_question:
            question = "Continue? [y/n] "

        input_ = input(question)
        terminal_clean()

        if input_ == "y" or input_ == "":

            while not is_game_finished:
                print("Default settings (Between 0-100, 10 attempts)")
                selection = input("Proceed with the default settings? [y/n] ")
                state = default_game_menu(selection)

                # Doğru ise evet veya hayır durumuna göre oyunu ayarlar
                if state:

                    terminal_clean()
                    # string lerin içi boş ise False değeri döndürürler
                    # selection objesisi string dir
                    if selection == "y" or selection == "Y" or not selection:
                        game()
                        is_game_finished = True
                    elif selection == "n" or selection == "N":
                        while True:
                            try:
                                x = int(input("First Number : "))
                                y = int(input("Last Number : "))
                                z = int(input("Guess attempts : "))
                                terminal_clean()

                                # İlk sayı, ikinci sayıdan küçük olmama durumu kontrolü
                                if x >= y:
                                    print("First number must be greater than last number (x > y)",
                                          str(29*'*'), sep="\n")
                                elif x < 0:
                                    print("First number must be above 0 or equal", str(29*'*'), sep='\n')
                                elif y > 1000:
                                    print("Last number can't exceed the limit (limit = 1000)", str(29*'*'), sep='\n')
                                # Deneme hakkının sınırı
                                elif z > 100:
                                    print("Guess attempts musn't exceed the limit (limit = 100)", str(29*'*'), sep='\n')
                                else:
                                    game(x, y, z)
                                    is_game_finished = True
                                    break

                            except (ValueError, TypeError):
                                terminal_clean()
                                print("Incorrect input", str(29*'*'), sep='\n')

                else:
                    terminal_clean()


        elif input_ == "n":
            print("Closing the app...")
            time.sleep(1)
            exit(0)

        elif input_ == "mrugur":
            print("Cultured gaming", "Cultured gaming", sep="\n")

        else:
            print("Incorrect input!")

        is_game_finished = False
        if not continue_question:
            continue_question = True
