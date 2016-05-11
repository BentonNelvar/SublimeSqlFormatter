import sublime
import sublime_plugin
from FormatSql import FormatSql
  
class FormatSqlCommand(sublime_plugin.TextCommand):
    
    def run(self, edit):
        formatSql = FormatSql()
        input = self.view.substr(sublime.Region(0, self.view.size()))
        if not input:
            print( 'No text to parse' )
        else:
            output = formatSql.format( input )
            print(output)

