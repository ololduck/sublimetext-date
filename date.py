import sublime, sublime_plugin
from datetime import datetime

class DateCommand(sublime_plugin.TextCommand):
	"""Prints Date + H:M"""
	def run(self, edit):
		self.view.insert(
			edit,
			self.view.sel()[0].begin(),
			datetime.now().strftime("%d/%m/%Y %H:%M")
			)

class HourCommand(sublime_plugin.TextCommand):
	"""Prints only H:M"""
	def run(self, edit):
		self.view.insert(
			edit,
			self.view.sel()[0].begin(),
			datetime.now().strftime("%H:%M")
			)
		