########################################################Modules#########################################################
# tkinter_modules
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

# os modules
import os

# screen_brightness_control_modules
import screen_brightness_control as sbc

# requests_modules
import requests

# web_browser_modules
import webbrowser

# pystray_modules
import pystray
from pystray import MenuItem as item

# PIL_modules
from PIL import Image

##########################################################Info##########################################################

title = 'Brightness Control'
version = 1.2

##########################################################GUI###########################################################
# full_process
def full_process():
    # tkinter_window
    root = tk.Tk()
    # window_title
    root.title(title)
    # program_icon
    root.iconbitmap(r'data\icons\Brightness Control.ico')
    # icon_system_tray
    icon_system_tray = Image.open(r'data\icons\Brightness Control.ico')
    # window_resize
    root.resizable(False, False)
    # window_center
    root.eval('tk::PlaceWindow . center')

    # update_checker_online
    def update_checker_online():
        if float(version_check) > float(version):
            webbrowser.open_new_tab(
                'https://github.com/muyeed15/Brightness-Control-Updates/blob/master/Brightness_Control_'
                'Update.exe?raw=true')
        else:
            messagebox.showinfo(title, 'You are running the latest version !')

    # update_checker_offline
    def update_checker_offline():
        messagebox.showinfo(title, 'Please check your internet connection !\nUnable to check for updates !')

    # startup
    try:
        try:
            # version_checker
            version_check_request = requests.get(
                'https://raw.githubusercontent.com/muyeed15/Brightness-Control-Updates/mas'
                'ter/version.txt')
            version_check = version_check_request.text
            # version_writer
            written_version = open(r'data\scripts\written_version.txt', 'w')
            written_version.write(version_check)
            written_version.close()
            # version_reader
            reading_version = open(r'data\scripts\written_version.txt', 'r')
            value_version = reading_version.read()

            if float(value_version) > float(version):
                # root_geometry
                root.geometry('325x139')
                # update_button_text
                update_button_text = 'Install Updates'
                version_or_update = 'Updates are available !\nCurrent Version   :  ' + str(
                    version) + '\nLatest Version      :  ' + str(value_version)
                # Update_button
                update_button = ttk.Button(root, text=update_button_text, command=update_checker_online)
                update_button.grid(row=2, column=2, ipadx=21, ipady=2)
                # update_notifier
                update_notifier = ttk.Label(root, text=version_or_update, foreground='red')
                update_notifier.grid(row=1, column=2)
            else:
                # root_geometry
                root.geometry('325x114')
                # update_button_text
                update_button_text = 'Check Updates'
                version_or_update = 'Version :  ' + str(version)
                # Update_button
                update_button = ttk.Button(root, text=update_button_text, command=update_checker_online)
                update_button.grid(row=2, column=2, ipadx=20, ipady=2)
                # update_notifier
                update_notifier = ttk.Label(root, text=version_or_update)
                update_notifier.grid(row=1, column=2, ipady=10)
        except:
            # version_reader
            reading_version = open(r'data\scripts\written_version.txt', 'r')
            value_version = reading_version.read()

            if float(value_version) > float(version):
                # root_geometry
                root.geometry('325x139')
                # update_button_text
                update_button_text = 'Install Updates'
                version_or_update = 'Updates are available !\nCurrent Version   :  ' + str(
                    version) + '\nLatest Version      :  ' + str(value_version)
                # Update_button
                update_button = ttk.Button(root, text=update_button_text, command=update_checker_offline)
                update_button.grid(row=2, column=2, ipadx=21, ipady=2)
                # update_notifier
                update_notifier = ttk.Label(root, text=version_or_update, foreground='red')
                update_notifier.grid(row=1, column=2)
            else:
                # root_geometry
                root.geometry('325x114')
                # update_button_text
                update_button_text = 'Check Updates'
                version_or_update = 'Version :  ' + str(version)
                # Update_button
                update_button = ttk.Button(root, text=update_button_text, command=update_checker_offline)
                update_button.grid(row=2, column=2, ipadx=20, ipady=2)
                # update_notifier
                update_notifier = ttk.Label(root, text=version_or_update)
                update_notifier.grid(row=1, column=2, ipady=10)

    except:
        # root_geometry
        root.geometry('325x114')
        # version_reader
        reading_version = open(r'data\scripts\written_version.txt', 'r')
        value_version = reading_version.read()
        # update_button_text
        update_button_text = 'Check Updates'
        version_or_update = 'Version :  ' + str(version)
        # Update_button
        update_button = ttk.Button(root, text=update_button_text, command=update_checker_offline)
        update_button.grid(row=2, column=2, ipadx=20, ipady=2)
        # update_notifier
        update_notifier = ttk.Label(root, text=version_or_update)
        update_notifier.grid(row=1, column=2, ipady=10)

    # slider_values
    slider_values = DoubleVar()

    # brightness_level
    brightness_level = ttk.Label(text='Brightness  :')
    brightness_level.grid(row=0, column=0, ipady=10, columnspan=1)

    # slider_values_operate
    def get_slider_values():
        return '{: .2f}'.format(slider_values.get())

    def slider_changed(event):
        # value_label
        value_label.config(text=get_slider_values())
        # brightness_control
        sbc.set_brightness(get_slider_values(), display=0)
        # value_writer
        written_value = open(r'data\scripts\written_value.txt', 'w')
        written_value.write(get_slider_values())
        written_value.close()

    # settings
    def settings():
        root_settings = tk.Tk()
        # root_settings_title
        root_settings.title('Settings')
        # root_settings_iconbitmap
        root_settings.iconbitmap(r'data\icons\Brightness Control.ico')
        # root_settings_resizable
        root_settings.resizable(False, False)
        # root_settings_window_center
        root_settings.eval('tk::PlaceWindow . center')

        # mail
        def mail():
            webbrowser.open('mailto:%20muyeed.al.abdullah@outlook.com')

        # GitHub
        def git():
            webbrowser.open('https://github.com/muyeed15')

        # startup_text
        reading_startup = open(r'data\scripts\startup.txt', 'r')
        value_startup = reading_startup.read()
        main_startup = 0.00
        if float(value_startup) > float(main_startup):
            startup_text = '   ↓ Click the button down below to not run Brightness Control in the start up ↓   '
            startup_button_text = 'Do not run in the start up'
        else:
            startup_text = '   ↓ Click the button down below to run Brightness Control in the start up ↓   '
            startup_button_text = 'Run in the start up'

        # startup_script
        def startup_script():
            if float(value_startup) > float(main_startup):
                # open_startup_del
                os.system(r'data\scripts\startup_del.bat')
                # write_startup
                written_startup = open(r'data\scripts\startup.txt', 'w')
                written_startup.write('0.00')
                written_startup.close()
                messagebox.showinfo(title, 'Brightness Control will not run in the startup !')
                root.destroy()
                root_settings.destroy()
            else:
                # open_startup
                os.system(r'data\scripts\startup.bat')
                # write_startup
                written_startup = open(r'data\scripts\startup.txt', 'w')
                written_startup.write('1.00')
                written_startup.close()
                messagebox.showinfo(title, 'Brightness Control will run in the startup !')
                root.destroy()
                root_settings.destroy()

        # restore_defaults
        def restore():
            # process_defaults
            process_write = open(r'data\scripts\process_info.txt', 'w')
            process_write.write('0.00')
            process_write.close()
            # startup_defaults
            written_startup = open(r'data\scripts\startup.txt', 'w')
            written_startup.write('1.00')
            written_startup.close()
            # brightness value
            written_value = open(r'data\scripts\written_value.txt', 'w')
            written_value.write('100.00')
            written_value.close()
            # startup_delete
            os.system(r'data\scripts\startup_del.bat')
            # restore_message
            messagebox.showinfo(title, 'Settings are now restored !')
            root.destroy()
            root_settings.destroy()

        # monitors label
        monito_label = ttk.Label(root_settings, text='↓ Connected Monitors ↓')
        monito_label.pack(ipady=5)
        # monitors list
        monitors = sbc.list_monitors()
        monitors_list_label = ttk.Label(root_settings, text=str(monitors), background='#F6931E')
        monitors_list_label.pack(ipady=5)
        # run at the start up
        run_satrt_up_label = ttk.Label(root_settings, text=startup_text)
        run_satrt_up_label.pack(ipady=5)
        run_satrt_up_button = ttk.Button(root_settings, text=startup_button_text, command=startup_script)
        run_satrt_up_button.pack(ipady=5)
        # border
        ttk.Label(root_settings, text='-------------------------------------------------------------------------------', foreground='#F6931E').pack(ipady=5)
        # restore_label
        restore_label = ttk.Label(root_settings, text='↓ Click the button down below to restore defaults ↓')
        restore_label.pack(ipady=5)
        # restore_button
        restore_button = ttk.Button(root_settings, text='Restore Defaults', command=restore)
        restore_button.pack(ipady=5)
        # border
        ttk.Label(root_settings, text='-------------------------------------------------------------------------------', foreground='#F6931E').pack(ipady=5)
        # brief
        ttk.Label(root_settings, text='Thank you for using Brightness Control !').pack(ipady=5)
        ttk.Label(root_settings, text='⚡ This program was developed by Muyeed ⚡').pack(ipady=5)
        Button(root_settings, text='☛ GitHub: https://github.com/muyeed15 ☚', command=git, borderwidth=0).pack(ipady=5)
        # feedback
        ttk.Label(root_settings, text='   ↓ Click the button down below to send feedbacks ↓   ').pack(ipady=10)
        ttk.Button(root_settings, text='Feedback', command=mail).pack(ipady=10, ipadx=20)
        root_settings.mainloop()

    # value_reader
    reading_value = open(r'data\scripts\written_value.txt', 'r')
    value_reader = reading_value.read()

    # brightness_at_startup
    sbc.set_brightness(value_reader)

    # value_label
    value_label = ttk.Label(root, text=get_slider_values())
    value_label.grid(row=1, column=1)

    # slider
    slider = ttk.Scale(root, from_=0, to=100, orient='horizontal', command=slider_changed, variable=slider_values)
    # slider_set
    slider.set(value_reader)
    slider.grid(row=0, column=1, columnspan=60, padx=40, ipadx=56, ipady=10)

    # value_amount
    value_amount = ttk.Label(root, text='Amount      :')
    value_amount.grid(row=1, column=0, columnspan=1)

    # settings_button
    settings_button = ttk.Button(root, text='Settings', command=settings)
    settings_button.grid(row=2, column=1, ipadx=25, ipady=2)

    # quit_window_function
    def quit_window(icon, item):
        icon.stop()
        root.destroy()

    # show_window_function
    def show_window(icon, item):
        icon.stop()
        root.after(0, root.deiconify())

    # hide_window_function
    def hide_window():
        root.withdraw()
        menu = (item(str(title), show_window, default=True), item('Quit', quit_window))
        icon = pystray.Icon(str(title), icon_system_tray, str(title), menu)
        icon.run()

    root.protocol('WM_DELETE_WINDOW', hide_window)

    root.mainloop()

def startup_writer():
    process_write = open(r'data\scripts\process_info.txt', 'w')
    process_write.write('1.00')
    process_write.close()

reading_process = open(r'data\scripts\process_info.txt', 'r')
process_code = reading_process.read()

try:
    minimize_code = 1.00

    if float(process_code) < float(minimize_code):
        os.system(r'data\scripts\startup.bat')
        startup_writer()
        messagebox.showinfo(title, 'Thank You, for installing Brightness Control !')
        full_process()
    else:
        full_process()
except:
    pass