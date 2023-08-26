from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.button import MDFloatingActionButton, MDIconButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField

KV = '''
BoxLayout:
    orientation: 'vertical'

    MDToolbar:
        title: 'ToDo List'

    ScrollView:
        MDList:
            id: todo_list

    MDFloatingActionButton:
        icon: "plus"
        pos_hint: {'center_x': 0.5}
        on_release: app.show_add_dialog()
'''

class TaskItem(OneLineAvatarIconListItem):
    pass

class ToDoApp(MDApp):
    def build(self):
        self.dialog = None
        return Builder.load_string(KV)

    def show_add_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Add Task",
                type="custom",
                content_cls=MDTextField(),
                buttons=[
                    MDIconButton(icon='cancel', on_release=self.close_dialog),
                    MDIconButton(icon='check', on_release=self.add_task),
                ],
            )
        self.dialog.open()

    def add_task(self, instance):
        task_text = self.dialog.content_cls.text.strip()
        if task_text:
            task_item = TaskItem(text=task_text)
            self.root.ids.todo_list.add_widget(task_item)
            self.dialog.content_cls.text = ""
            self.close_dialog()

    def close_dialog(self, instance=None):
        if self.dialog:
            self.dialog.dismiss()

if __name__ == '__main__':
    ToDoApp().run()
