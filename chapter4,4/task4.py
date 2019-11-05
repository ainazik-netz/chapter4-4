
class ContactList(list):
    def __init__(self, lst_, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.lst_ = lst_
    def search_by_name(self,name):
        
        lst_empty = []
        for i in self.lst:
            if i == name:
                lst_empty.append(name)
        print(lst_empty)
            
        ##должен принимать имя и возвращать список всех совпадений
all_contacts =  ContactList(['Altynbek', 'Akram', 'Gulzana', 'Uran'])
all_contacts.search_by_name('Akram')


