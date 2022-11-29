const dict = {
    "strona":"côté",
    "folder": "dossier",
    "klawiatura": "clavier",
    "żyrafa": "girafe",
    "buk": "hêtre",
    "komputer": "l'ordinateur",
    "ściana": "mur",
    "dom": "loger",
    "pies": "chien",
    "kot": "chat"
};

console.log(dict[process.argv[2]||"strona"]);