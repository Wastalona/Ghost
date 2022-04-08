import sqlite3

import datetime

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
    def get_data_from_db(what_get):
        i = 0
        for elems in cur.execute("""SELECT * FROM Wastalona"""):
            i += 1
        for elem in cur.execute(f"""SELECT {what_get} FROM Wastalona WHERE id = {i}"""):
            return elem[0]


    #func for button "ADD"
    def cancel(self):
        self.dialog.dismiss()


    def accept(self, bank, name_of_bank):
        global cash
        global id

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

        # data_for_db = (4, cash, date)
        # cur.execute("""INSERT INTO Wastalona VALUES(?,?,?);""", data_for_db)
        # db.commit()
        print(cash)


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

    #func for button "MENU"
    def all_budget():
        pass


    def charts():
        pass


    def theme():
        pass


    def cod():
        pass


    def about_of_us():
        pass


    def currency_converter(self, currency, money):
        if currency == 'USD':
            money = round(money * 0.31, 2)
            return money
        else:
            money = round(money * 0.29, 2)
            return money


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


    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        print(tab_text)


    def build(self):
        return Builder.load_file("data/interface.kv")


    global cash
    global cur
    global db
    # now = datetime.datetime.now()
    # date = now.strftime("%d-%m-%Y %H:%M")


    db = sqlite3.connect(r'data/ghostdb.db')
    cur = db.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS Wastalona(
        id INT PRIMARY KEY,
        wallet_balance FLOAT,
        date_of_issue TEXT
    )""")

    # cur.execute("""INSERT INTO Wastalona VALUES(?,?,?);""", data_for_db)

    db.commit()


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

GhostApp().run()
