import sublime, sublime_plugin  
  
class FormatSqlCommand(sublime_plugin.TextCommand):
    def run(self, edit):
    	for selector in self.view.sel():
        	self.view.insert(edit, selector.begin(), "Hello, World!\n")