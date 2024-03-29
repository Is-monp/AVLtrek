import flet as ft
import sys
#funciones de comportamiento
def theme_changed(e, page,slider):
    page.theme_mode = (
        ft.ThemeMode.DARK
        if page.theme_mode == ft.ThemeMode.LIGHT
        else ft.ThemeMode.LIGHT
    )
    slider.label = (
        "Light theme" if page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
    )
    page.update()

#Objetos de la GUI
def Slider(page):
    slider = ft.Switch(active_color=ft.colors.BLACK,label="Light theme", on_change=lambda e: theme_changed(e, page,slider))
    return slider

def images_slider(route_list, images):
    for route in route_list:
        images.controls.append(
            ft.Image(
                src=route,
                width=160,
                height=200,
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
            )
        )

def tree_display(image_path:str):
    main_display=ft.Container(
        content=ft.Image(
            src=image_path,
            width=800,
            height=650,
            fit=ft.ImageFit.COVER,
            repeat=ft.ImageRepeat.NO_REPEAT,
            border_radius=ft.border_radius.all(10)
        ),
        margin=5,
        padding=0,
        alignment=ft.alignment.center,
        width=800,
        height=650, 
        border_radius=ft.border_radius.all(10),       
    ) 
    return main_display