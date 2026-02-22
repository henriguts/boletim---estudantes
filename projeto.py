import tkinter as tk

# ---------------- JANELA ----------------
janela = tk.Tk()
janela.title("Boletim Escolar")
janela.geometry("600x650")
janela.resizable(False, False)

# ---------------- FUNÇÃO ----------------
def calcular_status(nota):
    return "APROVADO" if nota >= 6 else "REPROVADO"

# ---------------- DADOS ----------------
materias = [
    "Português", "Matemática", "Física", "Biologia",
    "Química", "História", "Geografia", "Sociologia",
    "Inglês", "Arte", "Ed. Física", "Filosofia"
]

entradas = {}

# ---------------- TÍTULO ----------------
titulo = tk.Label(
    janela,
    text="Boletim Escolar",
    font=("Arial", 20, "bold")
)
titulo.pack(pady=15)

# ---------------- FORMULÁRIO ----------------
frame_form = tk.Frame(janela)
frame_form.pack(pady=10)

for i, materia in enumerate(materias):
    tk.Label(
        frame_form,
        text=materia,
        anchor="w",
        width=15
    ).grid(row=i, column=0, padx=10, pady=5)

    entrada = tk.Entry(frame_form, width=10, justify="center")
    entrada.grid(row=i, column=1, padx=10, pady=5)

    entradas[materia] = entrada

# ---------------- RESULTADO ----------------
frame_resultado = tk.Frame(janela)
frame_resultado.pack(pady=20)

resultado = tk.Label(
    frame_resultado,
    text="",
    font=("Arial", 11),
    justify="left"
)
resultado.pack()

# ---------------- BOTÃO ----------------
def gerar_boletim():
    texto = ""
    for materia in materias:
        nota = float(entradas[materia].get())
        status = calcular_status(nota)
        texto += f"{materia} — {nota:.1f} — {status}\n"

    resultado.config(text=texto)

botao = tk.Button(
    janela,
    text="Gerar Boletim",
    font=("Arial", 11, "bold"),
    width=20,
    command=gerar_boletim
)
botao.pack(pady=15)

janela.mainloop()