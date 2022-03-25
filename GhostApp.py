from kivymd.app import MDApp
from kivymd.icon_definitions import md_icons
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivymd.theming import ThemableBehavior
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.uix.tab import MDTabsBase


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


class GhostApp(MDApp):
    title = "Ghost Money"
    cash = "607,34"

    data = {
        'income cash': 'cash-plus',
        'expences cash': 'cash-minus',
        'income card': 'credit-card-plus',
        'expences card': 'credit-card-minus',
    }


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


GhostApp().run()
