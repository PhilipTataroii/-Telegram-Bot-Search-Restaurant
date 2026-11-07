# 🤖 Telegram Bot — Căutare Restaurante

🌐 **Limbi disponibile pentru documentație**

🇬🇧 [English](README.md) | 🇷🇺 [Русский](README.ru.md) | 🇷🇴 **Română**

## 📖 Prezentare generală

Telegram Bot — Restaurant Search este un bot Telegram dezvoltat în Python, care ajută utilizatorii să găsească restaurante în funcție de tipul bucătăriei și preferințele alimentare.

Botul permite căutarea restaurantelor, afișarea informațiilor despre acestea și consultarea istoricului căutărilor anterioare.

Aplicația a fost realizată ca proiect educațional de diplomă în Python și demonstrează competențe practice în integrarea Telegram Bot API, gestionarea comenzilor, lucrul cu bazele de date și interacțiunea cu utilizatorii.

## ✨ Funcționalități

- 🔍 Căutarea restaurantelor după tipul bucătăriei sau cuvinte-cheie
- 🍣 Căutarea restaurantelor cu sushi, pizza și alte preparate
- 🏠 Afișarea numelui, adresei și fotografiilor disponibile ale restaurantului
- 📜 Salvarea istoricului căutărilor
- 🗂️ Vizualizarea căutărilor anterioare
- 🤖 Gestionarea comenzilor Telegram
- 👋 Mesaj de bun venit și informații de ajutor

## 📖 Comenzi disponibile

| Comandă | Descriere |
|---|---|
| `/start` | Pornirea botului și afișarea mesajului de bun venit |
| `/help` | Afișarea comenzilor disponibile |
| `/find <cuisine>` | Căutarea restaurantelor după tipul bucătăriei |
| `/history` | Vizualizarea istoricului căutărilor |

### Exemple de utilizare

```text
/start
/help
/find sushi
/find pizza
/history
```

## 🛠 Tehnologii utilizate

- **Limbaj de programare:** Python
- **Telegram API:** Aiogram
- **Bază de date:** SQLite
- **ORM:** Peewee
- **Cereri HTTP:** Requests
- **Controlul versiunilor:** Git, GitHub

## 🚀 Instalare și pornire

### 1. Clonarea repository-ului

```bash
git clone https://github.com/PhilipTataroii/Telegram-Bot-Search-Restaurant.git
cd Telegram-Bot-Search-Restaurant
```

### 2. Crearea unui mediu virtual

```bash
python -m venv .venv
```

Activarea în Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

În Linux/macOS:

```bash
source .venv/bin/activate
```

### 3. Instalarea dependențelor

```bash
pip install -r requirements.txt
```

### 4. Configurarea tokenului Telegram

Deschideți fișierul:

`Token_and_Database/config.py`

Configurați tokenul botului Telegram:

```python
BOT_TOKEN = "your_bot_token"
```

Tokenul poate fi obținut prin intermediul botului oficial @BotFather din Telegram.

**Securitate:** nu publicați niciodată tokenul real într-un repository public. Pentru utilizarea în producție, se recomandă păstrarea acestuia în variabile de mediu sau într-un fișier local exclus din Git.

### 5. Pornirea botului

```bash
python Start_Bot/bot.py
```

## 🔎 Testarea botului

După pornirea aplicației, deschideți botul în Telegram și executați comenzile:

| Comandă | Rezultat așteptat |
|---|---|
| `/start` | Afișează mesajul de bun venit |
| `/help` | Afișează lista comenzilor |
| `/find sushi` | Caută restaurante cu sushi |
| `/find pizza` | Caută pizzerii |
| `/history` | Afișează istoricul căutărilor |

Botul trebuie să ruleze local sau pe un server pentru a răspunde la comenzi.

## 📂 Structura proiectului

```text
Telegram-Bot-Search-Restaurant/
├── Handlers_Bot/
│   ├── start.py
│   ├── help.py
│   ├── find.py
│   └── history.py
├── Start_Bot/
│   └── bot.py
├── Token_and_Database/
│   └── config.py
├── requirements.txt
├── README.md
├── README.ru.md
└── README.ro.md
```

## 🗄️ Baza de date

Aplicația utilizează SQLite pentru stocarea istoricului căutărilor utilizatorilor.

Interacțiunea cu baza de date este realizată prin Peewee ORM.

## 📝 Note privind dezvoltarea

Acest proiect a fost dezvoltat în scopuri educaționale și pentru prezentarea competențelor practice de programare Python.

Botul Telegram rulează local și necesită un proces Python activ pentru a răspunde la mesaje.

Pentru disponibilitate permanentă, aplicația poate fi implementată pe un server cu o configurație corespunzătoare.

## 👨‍💻 Autor

**Filip Tataroi**

Python Developer

GitHub: https://github.com/PhilipTataroii

LinkedIn: https://www.linkedin.com/in/filip-tataroi/

**Tipul proiectului:** Proiect educațional de diplomă în Python
