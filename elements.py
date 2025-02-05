import flet as ft
from update import update_one


color1 = "#0f171f"
color2 = "#0b1b2b"
color3 = "#071636"
color4 = "#21354f"
color5 = "#476395"
color6 = "#798fb4"
color7 = ft.Colors.with_opacity(0.5, "#476395")
color8 = "#9cacca"

black1 = ft.Colors.with_opacity(0.4, "#000000")
black2 = ft.Colors.with_opacity(0.8, "#000000cc")
black3 = "#1b1b1b"
black4 = "#202020"
black5 = "#070B0F"
black6 = "#090F1C"

small_container_size = 0.25

def text_field():
        return ft.TextField(
            border_radius=6,
            bgcolor=black1,
            label_style=ft.TextStyle(color=color6),
            text_style=ft.TextStyle(color=color8, weight=ft.FontWeight.W_200),
            border_width=1,
            border_color=color4,
        )


def fade_container():
        return ft.Container(
            border=ft.border.all(1, color5),
            padding=15,
            border_radius=8,
            bgcolor=black5,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=[color2, color3, black5],
                stops=[0.0, 0.5, 1.0]
            ),
        )


def small_container(width):
        return ft.Container(
            border_radius=8,
            bgcolor=black1,
            border=ft.border.all(1, color=color4),
            padding=15,   
            width=width*small_container_size,
        )


def button(text):
        return ft.Button(
            text=text,
            style=ft.ButtonStyle(
                padding=ft.padding.symmetric(6, 10),
                shape=ft.RoundedRectangleBorder(radius=6),
                bgcolor={"": black1, "hovered": color3},
                side=ft.BorderSide(1, color5)
            )
        )


def card(id, name, current, target, img, handleClick):

    if float(current) > float(target):
        bordercolor = color5
        gradientcolor = color3
    else:
        bordercolor = "#479580"
        gradientcolor = "#07362b"

    return ft.Stack([
        ft.Image(
            src=img,
            height=170,
            width=170,
            fit=ft.ImageFit.FILL,
            border_radius=8,
        ),
        ft.Container(
            width=170,
            height=170,
            ink=True,
            padding=10,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=[ft.Colors.with_opacity(0.7, gradientcolor), gradientcolor],
                stops=[0.0, 1]
            ),
            on_click=handleClick,
            border_radius=8,
            border=ft.border.all(1, bordercolor),
            content=ft.Column(
                controls=[
                    ft.Text(name+"\n\n", max_lines=3, expand=1),        
                    ft.Text(value=f"R${current} currently\nR${target} target"),
                ]
            ),
        )

    ], width=170, height=170, key=id)


def modal_field():
        return ft.TextField(
            border_radius=6,
            bgcolor=black6,
            label_style=ft.TextStyle(color=color8),
            text_style=ft.TextStyle(color=color8, weight=ft.FontWeight.W_400),
            border_width=1,
            border_color=color5,
        )

def new_modal():
    modal_title = modal_field()
    modal_title.expand = 1

    modal_target = modal_field()
    modal_target.prefix_text = "$"
    modal_target.width = 85

    modal_link = modal_field()

    def handleCancel(e: ft.ControlEvent):
        e.page.close(cancelbt.parent.parent.parent.parent.parent)

    bgimage = ft.Image(
        height=200,
        width=400,
        src="",
        fit=ft.ImageFit.COVER,
        border_radius=8,
    )

    savebt = button("save")
    openbt = button("open in browser")
    cancelbt = button("cancel")
    cancelbt.on_click = handleCancel
    deletebt = button("delete")

    newmodal = ft.AlertDialog(
        modal=False,
        barrier_color=ft.Colors.BLACK45,
        bgcolor=ft.Colors.TRANSPARENT,
        shape=ft.RoundedRectangleBorder(8),
        content=ft.Stack(
            controls=[
                bgimage,
                ft.Container(
                    height=200,
                    width=400,
                    padding=20,
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=[ft.Colors.with_opacity(0.7, color3), color3],
                        stops=[0.0, 1]
                    ),
                    border_radius=8,
                    border=ft.border.all(1, color5),
                    content=ft.Column(
                        alignment=ft.alignment.center,
                        controls=[    
                            ft.Row(
                                controls=[
                                    modal_title,
                                    modal_target
                                ]
                            ),
                            modal_link,
                            ft.Row(
                                
                                controls=[
                                    openbt,
                                    savebt,
                                    deletebt,
                                    cancelbt
                                ]
                            )
                        ]
                    )
                ),
            ]
        ),
    )
#              0           1            2             3         4       5       6        7       
    return [newmodal, modal_title, modal_target, modal_link, bgimage, savebt, openbt, deletebt]


def addForm():
    
    def handleCancel(e: ft.ControlEvent):
        modal = e.control.parent.parent.parent.parent.parent
        e.page.close(modal)
        e.page.update()

    width = 400

    add_link = text_field()
    add_title = text_field()
    add_target = text_field()
    add_button = button("add")
    cancelbt = button("cancel")
    cancelbt.on_click = handleCancel

    add_link.label = "link"
    add_link.value = ""

    add_title.width = width*small_container_size*0.1
    add_title.expand = 1
    add_title.label = "title"
    add_title.value = ""

    add_target.width = width*small_container_size
    add_target.label = "target"
    add_target.prefix_text = "$"
    add_target.value = ""

    bg = fade_container()
    bg.width = 440
    bg.height = 240
    content = small_container(width)
    content.width = 400
    content.height = 200

    content.content = ft.Column(
        controls=[
            ft.Text(value="add new to list", color=color6),
            add_link,
            ft.Row(
                controls=[
                    add_title, 
                    add_target,
                ]),
            ft.Row(controls=[add_button, cancelbt])
            
        ]
    )

    bg.content = content

    addModal = ft.AlertDialog(
        modal=False,
        barrier_color=ft.Colors.BLACK45,
        bgcolor=ft.Colors.TRANSPARENT,
        content=bg
    )
#              0          1           2          3         4
    return [addModal, add_title, add_target, add_link, add_button]