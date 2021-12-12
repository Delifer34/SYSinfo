#Библиотеки для работы приложения
#Библиотека sg для интерфейса а библиотка platform для команд внутри системы
import PySimpleGUI as sg
import platform


#Дизайн и вывод на экран

sg.theme('DarkGrey5')

layout = [
	[sg.Text("\t\t\t      🆂🆈🆂🅸🅽🅵🅾", font=30)],
	[sg.Radio("Linux", "RADIO1", default=False, key="r1", visible=True)],[sg.Radio("Windows", "RADIO2", default=False, key="r2", visible=True)],
	[sg.Text("\t\t\t        "), sg.Button("Начать сбор информации", key="start", visible=True, font=17)],
	[sg.Text("Ифнормация о системе:", key="txtuinfo", visible=False,font=30)],
	#Все кнопки сначала спрятаны но потом они появятся из результата выбора пользователем
	#Linux
	[sg.Text("Архитектура:", key="txtplatform", visible=False,font=30)],
	[sg.Text(platform.architecture(), key="sysplatform", visible=False)],
	[sg.Text("Тип машины:", key="txtmachine", visible=False,font=30)],
	[sg.Text(platform.machine(), key="sysmachine", visible=False)],
	[sg.Text("Сетевое имя компьютера:", key="txtnode", visible=False,font=30)],
	[sg.Text(platform.node(), key="sysnode", visible=False)],
	[sg.Text("Сведения о базовой платформе:", key="txtplatform2", visible=False,font=30)],
	[sg.Text(platform.platform(), key="sysplatform2", visible=False)],
	[sg.Text("Реальное имя процессора:", key="txtproc", visible=False,font=30)],
	[sg.Text(platform.processor(), key="sysproc", visible=False)],
	[sg.Text("Сведения о выпуске системы:", key="txtrelease", visible=False,font=30)],
	[sg.Text(platform.release(), key="sysrelease", visible=False)],
	#Windows
	[sg.Text("Информация о версии из реестра Windows:", key="txtwin32", font=30, visible=False)],
	[sg.Text(platform.win32_ver(), key="win32", visible=False)],
	[sg.Text("Текущая редакция Windows: ", key="txtwin32ed", font=30, visible=False)],
	[sg.Text(platform.win32_edition(), key="win32ed", visible=False)]
]

window = sg.Window("SYSinfo", layout, icon=r'logosysinfo.png', size=(700,650), finalize=True) #моделироваение экрана

while True:
	event, values = window.read() #чтение боксов и регистация действий с экрана
	if event == "start": #Команда нажатия на кнопку
		if values["r1"] == True: #Если выбрана ОС линукс то информация для неё
			window.Refresh()
			window["txtplatform2"].update(visible=True) #Текст
			window["sysplatform2"].update(visible=True) #команда
			window["txtuinfo"].update(visible=True) #Текст
			window["txtplatform"].update(visible=True) #Текст
			window["sysplatform"].update(visible=True) #команда
			window["txtmachine"].update(visible=True) #Текст
			window["sysmachine"].update(visible=True) #команда
			window["txtnode"].update(visible=True) #Текст
			window["sysnode"].update(visible=True) #команда
			window["txtrelease"].update(visible=True) #Текст
			window["sysrelease"].update(visible=True) #команда
		if values["r2"] == True: #Если выбрана для Виндовс то информация для неё
			window["txtwin32"].update(visible=True) #Текст
			window["win32"].update(visible=True) #команда
			window["txtwin32ed"].update(visible=True) #Текст
			window["win32ed"].update(visible=True) #команда

		window["start"].update(visible=False) #Прячем кнопку старт
		window["r1"].update(visible=False)	#Прячем кнопкy линукс
		window["r2"].update(visible=False)	#Прячем кнопку виндовс
		
	if event == sg.WIN_CLOSED: #закрытие программы
		break
	
	window.Refresh() #обновление экрана

window.close() #закрытие окна
