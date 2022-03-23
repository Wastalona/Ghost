from kivymd.app import MDApp
from kivymd.icon_definitions import md_icons
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivymd.theming import ThemableBehavior
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.uix.tab import MDTabsBase



KV = '''
# Menu item in the DrawerList list.
<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)

    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color


<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "data/image/statistics.png"

    MDLabel:
        text: "Settings"
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]


    ScrollView:
        DrawerList:
            id: md_list


Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: "Ghost Money"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
                        md_bg_color:.17,.18,.18,1

                    MDTabs:
                        id: tabs
                        on_tab_switch: app.on_tab_switch(*args)
                        height:"48dp"
                        tab_indicator_anim: False
                        background_color:.1,.1,.1,1

                        Tab:
                            id: 1
                            title: "History"
                            icon: "view-list"
                            BoxLayout:
                                orientation: 'vertical'
                                padding: "5dp"

                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDLabel:
                                        text: "History"
                                        halign: "center"

                        Tab:
                            id: 2
                            title: "Expences"
                            icon: "star"
                            BoxLayout:
                                orientation: 'vertical'
                                padding: "5dp"

                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDLabel:
                                        text: "Necessary"
                                        halign: "center"


                        Tab:
                            id: 3
                            title: "Income"
                            icon: "penguin"
                            BoxLayout:
                                orientation: 'vertical'
                                padding: "5dp"

                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDLabel:
                                        text: "Unnecessary"
                                        halign: "center"


                        Tab:
                            id: 4
                            title: "Storage"
                            icon: "safe-square"
                            BoxLayout:
                                orientation: 'vertical'
                                padding: "5dp"

                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDLabel:
                                        text: "Storage"
                                        halign: "center"


    MDNavigationDrawer:
        id: nav_drawer
        md_bg_color:.99,.98,.98,1

        ContentNavigationDrawer:
            id: content_drawer


    MDScreen:
        MDFloatingActionButtonSpeedDial:
            data: app.data
            root_button_anim: True
        MDFloatingActionButtonSpeedDial:
            hint_animation: True
'''


class Tab(MDFloatLayout, MDTabsBase):
    pass


class ContentNavigationDrawer(BoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class testApp(MDApp):
    data = {
        'income cash': 'cash-plus',
        'expences cash': 'cash-minus',
        'income card': 'credit-card-plus',
        'expences card': 'credit-card-minus',
    }

    def build(self):
        return Builder.load_string(KV)

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
        # #add tabs
        # self.root.ids.tabs.add_widget(Tab(icon="view-list", title="History"))
        # self.root.ids.tabs.add_widget(Tab(icon="star", title="Necessary"))
        # self.root.ids.tabs.add_widget(Tab(icon="penguin", title="Unnecessary"))
        # self.root.ids.tabs.add_widget(Tab(icon="safe-square", title="Storage"))


    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        print(tab_text)


testApp().run()
