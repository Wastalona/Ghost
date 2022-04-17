#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~import library~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import sqlite3

import datetime
import webbrowser

from kivymd.app import MDApp
from kivymd.icon_definitions import md_icons
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivymd.theming import ThemableBehavior
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.button import MDFloatingActionButtonSpeedDial
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.picker import MDDatePicker
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Tab(MDFloatLayout, MDTabsBase):
    pass


class ContentNavigationDrawer(BoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((.98, .96, .90, 1))


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""
        pass
        # Set the color of the icon and text for the menu item.
        # for item in self.children:
        #     if item.text_color == self.theme_cls.primary_color:
        #         item.text_color = self.theme_cls.text_color
        #         break
        # instance_item.text_color = self.theme_cls.primary_color


class Content(BoxLayout):
    pass


class GhostApp(MDApp):
#========================func to get data from data base=======================
    def get_data_from_db(what_get):
        i = 0
        for elems in cur.execute("""SELECT * FROM Wastalona"""):
            i += 1
        for elem in cur.execute(f"""SELECT {what_get} FROM Wastalona WHERE id = {i}"""):
            return elem[0]
#===============================================================================


    #################################variable##################################
    global cash
    global cur
    global db
    global id
    # now = datetime.datetime.now()
    # hy = now.strftime("%d-%m-%Y %H:%M")


    db = sqlite3.connect(r'data/ghostdb.db')
    cur = db.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS Wastalona(
        id INT PRIMARY KEY,
        wallet_balance FLOAT,
        date_of_issue TEXT
    )""")
    # data_for_db = (1, 600, hy)

    # cur.execute("""INSERT INTO Wastalona VALUES(?,?,?);""", data_for_db)
    #
    # db.commit()


    id = get_data_from_db("id")
    cash = get_data_from_db("wallet_balance")
    date = get_data_from_db("date_of_issue")


    cash50 = round(cash * 0.5, 2)
    cash30 = round(cash * 0.3, 2)
    cash20 = round(cash * 0.2, 2)
    # data_for_db = (1,cash, date)

    title = "Ghost Money"
    dialog = None

    data = {
        'income cash': 'cash-plus',
        'expences cash': 'cash-minus',
        'income card': 'credit-card-plus',
        'expences card': 'credit-card-minus',
    }

    # Theme_Checking()
    ##########################################################################


#============================func for button "ADD"==============================
    def cancel(self):
        self.dialog.dismiss()


    def accept(self, bank, name_of_bank):
        global cash
        global id


        def Update_Label(update_data_lab):
            new_nes_cash = round(update_data_lab * 0.5, 2)
            new_unes_cash = round(update_data_lab * 0.3, 2)
            new_srg_cash = round(update_data_lab * 0.2, 2)


            self.root.ids.nes_lab_byn.text = f"₽ {new_nes_cash} BYN"
            self.root.ids.nes_lab_usd.text = f"$ {round(new_nes_cash * 0.31, 2)} USD"
            self.root.ids.nes_lab_eur.text = f"€ {round(new_nes_cash * 0.29, 2)} EUR"

            self.root.ids.unes_lab_byn.text = f"₽ {new_unes_cash} BYN"
            self.root.ids.unes_lab_usd.text = f"$ {round(new_unes_cash * 0.31, 2)} USD"
            self.root.ids.unes_lab_eur.text = f"€ {round(new_unes_cash * 0.29, 2)} EUR"

            self.root.ids.srg_lab_byn.text = f"₽ {new_srg_cash} BYN"
            self.root.ids.srg_lab_usd.text = f"$ {round(new_srg_cash * 0.31, 2)} USD"
            self.root.ids.srg_lab_eur.text = f"€ {round(new_srg_cash * 0.29, 2)} EUR"


        now = datetime.datetime.now()
        date = now.strftime("%d-%m-%Y %H:%M")


        self.dialog.dismiss()
        print(name_of_bank, '~', bank)

        if bank.isdigit() is not True:
            bank = 0
        elif bar == 1:
            cash = round(cash + float(bank))
        else:
            cash = round(cash - float(bank))

        Update_Label(cash)

        # data_for_db = (id + 1, cash, date)
        # cur.execute("""INSERT INTO Wastalona VALUES(?,?,?);""", data_for_db)
        # db.commit()
        print(cash)


    def on_save(self, instance, value, date_range):
        print(value)


    def on_cancel(self, instance, value):
        print('close')


    def show_date_picker(self):
        date_dialog = MDDatePicker()
        primary_color= .56, .23, 1, 1
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()


    def call(self, btn):
        global bar
        def dialog_window():
            # if not self.dialog:
            self.dialog = MDDialog(
                title='Change in wallet',
                type="custom",
                content_cls=Content(),
                auto_dismiss=False,
            )
            self.dialog.open()


        if btn.icon == 'cash-plus' or btn.icon == 'credit-card-plus':
            bar = 1
            dialog_window()
        else:
            bar = 2
            dialog_window()
#===============================================================================


#============================func for button "MENU"=============================
    def Check_list(self, choose_func):
        global theme_count
        def all_budget():
            print("all_budget")
            # return Builder.load_file("data/interface_budget.kv")


        def charts():
            print("charts")


        def theme():
            def apply_theme(name_theme, cfg_count):
                self.theme_cls.theme_style = name_theme
                with open("cfg.txt", "w") as d:
                    d.seek(33)
                    d.write(cfg_count)

            with open("cfg.txt", "r") as f:
                f.seek(33)
                text = int(f.read(1))
                apply_theme("Dark", "1") if text == 0 else apply_theme("Light", "0")


        def send():
            print("send")


        def cod():
            webbrowser.open('https://github.com/Wastalona/Ghost', new=2)


        def about_of_us():
            print("about_of_us")


        name_of_tab = [
            'account-cash',
            'chart-arc',
            'theme-light-dark',
            'file-export',
            'github',
            'information-outline']

        # all_budget()
        # charts()
        # theme()
        # send()
        # about_of_us()
        if choose_func == 'github':
            cod()
        elif choose_func == 'account-cash':
            all_budget()
        elif choose_func == 'chart-arc':
            charts()
        elif choose_func == 'file-export':
            send()
        elif choose_func == 'theme-light-dark':
            theme()
        elif choose_func == 'information-outline':
            about_of_us()


    def currency_converter(self, currency, money):
        if currency == 'USD':
            return round(money * 0.31, 2)
        else:
            return round(money * 0.29, 2)


    def on_start(self):
        icons_item = {
            "account-cash": "All budget",
            "chart-arc": "Charts",
            "theme-light-dark": "Light/Dark",
            "file-export": "Export",
            "github": "Source code",
            "information-outline": "About of app",
        }
        for icon_name in icons_item.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name]))


    """
        ! Tab change check !
        def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        print(tab_text)
    """
#===============================================================================


#============================func for start interface===========================
    def build(self):
        with open("cfg.txt", "r") as f:
            f.seek(33)
            text = int(f.read(1))
            if text == 0: self.theme_cls.theme_style = "Light"  #else print("Dark")
            if text == 1: self.theme_cls.theme_style = "Dark"
        return Builder.load_file("data/interface.kv")
#===============================================================================

GhostApp().run()
