from guizero import App, PushButton, Text, Box

app = App(title="Concert audio monitor", bg="#000000",  )
whole_app_box = Box(app, align="bottom", height="fill", width="fill")

level_indic_box = Box(whole_app_box, align="top", width="fill")

top_pad = Box(level_indic_box, height=100, width="fill", align="top")

text_box = Box(level_indic_box, align="top", width="fill")
text = Text(text_box, text="96.1", color="#00E626", align="top",width="fill", size=600)

botom_pad = Box(level_indic_box, height=0, width="fill", align="bottom")

buttons_box = Box(whole_app_box, layout="grid")
reset_button = PushButton(buttons_box, command=None, text="Reset averaging", grid=[0,0], padx=30, pady=30)
fifteen_button = PushButton(buttons_box, command=None, text="15 minute average", grid=[1,0], padx=30, pady=30)
one_button = PushButton(buttons_box, command=None, text="1 minute average", grid=[2,0], padx=30, pady=30)
instant_button = PushButton(buttons_box, command=None, text="Instant SPL", grid=[3,0], padx=30, pady=30)

instant_button.text_color="#ffffff"
instant_button.text_size=20

one_button.text_color="#ffffff"
one_button.text_size=20

fifteen_button.text_color="#ffffff"
fifteen_button.text_size=20

reset_button.text_color="#ffffff"
reset_button.text_size=20

app.set_full_screen()
app.display()