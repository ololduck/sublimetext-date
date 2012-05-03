import sublime, sublime_plugin
from datetime import datetime

class DateCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit,
			self.view.sel()[0].begin(),
			datetime.now().strftime("%d/%m/%Y %H:%M")
			)