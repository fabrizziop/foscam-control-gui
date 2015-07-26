from tkinter import *
from tkinter import ttk
import time
import urllib.request
const_up = 0
const_down = 2
const_right = 4
const_left = 6
const_diag_up_left = 91
const_diag_up_right = 90
const_diag_down_left = 93
const_diag_down_right = 92
const_center = 25
const_led_on = 95
const_led_off = 94
class command_sender(object):
	def __init__(self):
		pass
	def update_data(self, fqdn, username, password):
		self.url = "http://"+fqdn+"/decoder_control.cgi?user="+username+"&pwd="+password+"&command="
		print(self.url)
	def send_movement(self, scale_num, mov_num):
		urllib.request.urlopen(self.url+str(mov_num))
		print(scale_num)
		time.sleep(scale_num*0.01)
		urllib.request.urlopen(self.url+"1")
	def send_single_command(self, mov_num):
		urllib.request.urlopen(self.url+str(mov_num))
		
		
def send_command_to_camera(command_type, flip, fqdn, username, password):
	url = "http://"+fqdn+"/decoder_control.cgi?user="+username+"&pwd="+password+"&command="
	if command_type == "LED_ON":
		pass
		#urllib.request.urlopen
	
class main_program_gui(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)
		self.parent = parent
		self.command_object = command_sender()
		self.init_ui()
		self.pack()
	def update_all(self):
		self.command_object.update_data(self.fqdn_var.get(),self.user_var.get(),self.pass_var.get())
		for bttn in self.button_list:
			bttn.state(["!disabled"])
	def send_up(self):
		if self.flip_var.get() == False:
			self.command_object.send_movement(self.scale_time.get(), const_up)
		else:
			self.command_object.send_movement(self.scale_time.get(), const_down)
	def send_down(self):
		if self.flip_var.get() == False:
			self.command_object.send_movement(self.scale_time.get(), const_down)
		else:
			self.command_object.send_movement(self.scale_time.get(), const_up)
	def send_left(self):
		if self.flip_var.get() == False:
			self.command_object.send_movement(self.scale_time.get(), const_left)
		else:
			self.command_object.send_movement(self.scale_time.get(), const_right)
	def send_right(self):
		if self.flip_var.get() == False:
			self.command_object.send_movement(self.scale_time.get(), const_right)
		else:
			self.command_object.send_movement(self.scale_time.get(), const_left)
	def send_diag_up_left(self):
		if self.flip_var.get() == False:
			self.command_object.send_movement(self.scale_time.get(), const_diag_up_left)
		else:
			self.command_object.send_movement(self.scale_time.get(), const_diag_down_right)
	def send_diag_up_right(self):
		if self.flip_var.get() == False:
			self.command_object.send_movement(self.scale_time.get(), const_diag_up_right)
		else:
			self.command_object.send_movement(self.scale_time.get(), const_diag_down_left)
	def send_diag_down_left(self):
		if self.flip_var.get() == False:
			self.command_object.send_movement(self.scale_time.get(), const_diag_down_left)
		else:
			self.command_object.send_movement(self.scale_time.get(), const_diag_up_right)
	def send_diag_down_right(self):
		if self.flip_var.get() == False:
			self.command_object.send_movement(self.scale_time.get(), const_diag_down_right)
		else:
			self.command_object.send_movement(self.scale_time.get(), const_diag_up_left)
	def send_center(self):
		self.command_object.send_single_command(const_center)
	def send_led_on(self):
		self.command_object.send_single_command(const_led_on)
	def send_led_off(self):
		self.command_object.send_single_command(const_led_off)
	def init_ui(self):
		self.parent.title("FI8918W PT Control")
		self.main_frame = ttk.Frame(self)
		self.button_list = []
		self.button_list.append(ttk.Button(self.main_frame,text="\u2196",state="disabled",command=self.send_diag_up_left))
		self.button_list.append(ttk.Button(self.main_frame,text="\u2191",state="disabled",command=self.send_up))
		self.button_list.append(ttk.Button(self.main_frame,text="\u2197",state="disabled",command=self.send_diag_up_right))
		self.button_list.append(ttk.Button(self.main_frame,text="\u2190",state="disabled",command=self.send_left))
		self.button_list.append(ttk.Button(self.main_frame,text="\u2022",state="disabled",command=self.send_center))
		self.button_list.append(ttk.Button(self.main_frame,text="\u2192",state="disabled",command=self.send_right))
		self.button_list.append(ttk.Button(self.main_frame,text="\u2199",state="disabled",command=self.send_diag_down_left))
		self.button_list.append(ttk.Button(self.main_frame,text="\u2193",state="disabled",command=self.send_down))
		self.button_list.append(ttk.Button(self.main_frame,text="\u2198",state="disabled",command=self.send_diag_down_right))
		self.button_list.append(ttk.Button(self.main_frame,text="ON",state="disabled",command=self.send_led_on))
		self.button_list[9].grid(row=3,column=0)
		ttk.Label(self.main_frame,text="LED").grid(row=3,column=1)
		self.button_list.append(ttk.Button(self.main_frame,text="OFF",state="disabled",command=self.send_led_off))
		self.button_list[10].grid(row=3,column=2)
		ttk.Label(self.main_frame,text="FQDN").grid(row=0,column=3)
		ttk.Label(self.main_frame,text="User").grid(row=1,column=3)
		ttk.Label(self.main_frame,text="Pass").grid(row=2,column=3)
		self.fqdn_var = StringVar()
		self.user_var = StringVar()
		self.pass_var = StringVar()
		self.flip_var = IntVar()
		self.fqdn_entry = ttk.Entry(self.main_frame,textvariable=self.fqdn_var)
		self.fqdn_entry.grid(row=0,column=4)
		self.user_entry = ttk.Entry(self.main_frame,textvariable=self.user_var)
		self.user_entry.grid(row=1,column=4)
		self.pass_entry = ttk.Entry(self.main_frame,textvariable=self.pass_var,show="*")
		self.pass_entry.grid(row=2,column=4)
		#ttk.Label(self.pack_frame,text="Flip").grid(row=0,column=0)
		self.flip_control = ttk.Checkbutton(self.main_frame, text="Flip", variable=self.flip_var)
		self.flip_control.grid(row=3,column=3)
		self.update_info = ttk.Button(self.main_frame, text="Update", command=self.update_all)
		self.update_info.grid(row=3,column=4)
		ttk.Label(self.main_frame, text="M. Am").grid(row=0,column=5)
		self.scale_time = ttk.Scale(self.main_frame, from_=10, to=200, orient="vertical")
		self.scale_time.grid(row=1,column=5, rowspan=4)
		c = 0
		for i in range(0,3):
			for j in range(0,3):
				self.button_list[c].grid(row=i,column=j)
				c += 1
		self.main_frame.pack()
		def update_all():
			pass

main_window = Tk()
actual_program = main_program_gui(main_window)
main_window.mainloop()
