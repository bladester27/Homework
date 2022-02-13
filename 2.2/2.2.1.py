class Editor:
    def __init__(self, doc):
        self.doc = doc

    def view_document(self):
        return open(self, 'r')

    def edit_document(self):
        return print('Не возможно в бесплатной версии')


class Proeditor(Editor):
    def __init__(self, doc):
        super(Editor, self).__init__(doc)

    def edit_document(self, lic=0):
        lic = str(input('Введи лицензию - '))
        if lic == '1234':
            return open(self, 'r+')
        else:
            return Editor.edit_document(self)


a = Editor.view_document('.gitignore')
b = Editor.edit_document('.gitignore')
z = Proeditor.view_document('.gitignore')
x = Proeditor.edit_document('.gitignore')
