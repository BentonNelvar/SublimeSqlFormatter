import sublime, sublime_plugin  
  
class FormatSqlCommand(sublime_plugin.TextCommand):
    index = 0

    def getNextWord( self ):
        if FormatSqlCommand.index < self.view.size():
            region , word = self.getWord( FormatSqlCommand.index )
            FormatSqlCommand.index = region.b + 1
            return region , word
        else:
            return None , None

    def getWord( self , index ):
        region = self.view.word( index )
        word = self.view.substr( region )
        return ( region , word )
    
    def run(self, edit):
        FormatSqlCommand.index = 0
        while True:
            region , word = self.getNextWord()
            if word == None or region == None:
                break
            else:
                self.view.replace( edit , region , word.upper() )

