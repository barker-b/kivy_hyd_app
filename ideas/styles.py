#:kivy 2.3.1

<FormulaScreen>:
    BoxLayout:
        orientation: "vertical"
        spacing: dp(12)
        padding: dp(20)
        canvas.before:
            Color:
                rgba: 0.08, 0.10, 0.12, 1   # dark background
            Rectangle:
                pos: self.pos
                size: self.size

        Label:
            text: "Hydraulic Formula Reference"
            font_size: "28sp"
            bold: True
            color: 0.95, 0.95, 0.95, 1
            size_hint_y: None
            height: self.texture_size[1]

        # --- Cylinder Section ---
        BoxLayout:
            orientation: "vertical"
            padding: dp(10)
            spacing: dp(6)
            canvas.before:
                Color:
                    rgba: 0.15, 0.18, 0.22, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [10]

            Label:
                text: "Cylinder Formulas"
                font_size: "22sp"
                bold: True
                color: 0.9, 0.9, 0.9, 1

            Label:
                text: "Bore Piston Area = π × r²\nRod Piston Area = Piston Area − Rod Area\nPush Force = Bore Area × Pressure\nPull Force = Rod Area × Pressure"
                font_size: "16sp"
                color: 0.85, 0.85, 0.85, 1

        # --- Motor Section ---
        BoxLayout:
            orientation: "vertical"
            padding: dp(10)
            spacing: dp(6)
            canvas.before:
                Color:
                    rgba: 0.15, 0.18, 0.22, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [10]

            Label:
                text: "Motor Formulas"
                font_size: "22sp"
                bold: True
                color: 0.9, 0.9, 0.9, 1

            Label:
                text: "Motor Torque = Pressure × Displacement ÷ 2π\nMotor Speed = 231 × Flow ÷ Displacement"
                font_size: "16sp"
                color: 0.85, 0.85, 0.85, 1

        # --- Pump Section ---
        BoxLayout:
            orientation: "vertical"
            padding: dp(10)
            spacing: dp(6)
            canvas.before:
                Color:
                    rgba: 0.15, 0.18, 0.22, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [10]

            Label:
                text: "Pump Formulas"
                font_size: "22sp"
                bold: True
                color: 0.9, 0.9, 0.9, 1

            Label:
                text: "Pump Flow = RPM × Displacement ÷ 231\nPump Horsepower = Flow × Pressure ÷ 1714\nDriving Torque = Pressure × Displacement ÷ 2π"
                font_size: "16sp"
                color: 0.85, 0.85, 0.85, 1

        Button:
            text: "Back"
            size_hint_y: None
            height: dp(50)
            font_size: "20sp"
            background_color: 0.25, 0.35, 0.45, 1
            color: 1, 1, 1, 1
            on_press: root.go_back()

# Playing with ideas

#:kivy 2.3.1
<FormulaScreen>:
    BoxLayout:
        orientation: "vertical"
        spacing : 5
        padding: 5
        Label:
            text: "Cylinder Formulas"

        Label:            
            text:
                "Bore Piston Area = π x r² \n\
                Rod Piston Area = Piston Area - Rod Area\n\
                Push Force = Bore Piston Area x Pressure\n\
                Pull Force = Rod Piston Area x Pressure"

        Label:
            text: "Motor Formulas"

        Label:
            text:
                "Motor Torque = Pressure x Displacement / 2π\n\
                Motor Speed = 231 x Flow / Displacement"

        Label:
            text: "Pump Formulas"

        Label:
            text:
                "Pump FLow = RPM x Displacement / 231\n\
                Pump Hose Power = Pump Flow x Presssure / 1,714\n\
                Driving Tourqe = Pressure x Displacement / 2π"
        Button:
            text: "Back"
            on_press: root.go_back()
