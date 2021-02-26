###class footbal:
    def __init__(self,name,age,kol,apl,lch):
        self.name=name
        self.age=age
        self.kol=kol
        self.apl=apl
        self.lch=lch

        def wean(self):
            print('Побеждают 9 из 10 случаях')
        def loss(self):
            print('Проигрывают один матч из 10')
my=footbal('Манчестер сити','Основан в 1888 году','Могут взять чемпионат без единного поражения','АПЛ им покорилась четырежды','Еще не пришло вермя')
print('Название команды: '+my.name,'Когда быол основан: '+my.age,'Сколько раз они взяли родной чемпионат: '+my.apl,'Как обстоят дела с лч:'+my.lch,sep='\n')
