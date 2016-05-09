import sublime, sublime_plugin  
  
class FormatSqlCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        index = 0
        while( index < view.size() ):
            region , word = getWord( view , index )
            view.replace( edit , region , word.upper() )
            index = region.b + 1

def getWord( view , index ):
    region = view.word( index )
    word = view.substr( region )
    return ( region , word )
