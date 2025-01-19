# Day01: 17-Jan-2025

> `windows + h` 🤔

## Intro

- `Instruction` command given to a computer to perform a particular task
    - eg: print("Hello") or x = 5

- `Program` a set/collection of instructions 
    - eg: program to print sum of two integers

- `Software` a collection of multiple programs
    - eg: calculator

```
Think of it as:

Instruction → Single brick
Program → Wall made of bricks
Software → Complete building
```

## Types of Software

```
User
  ↓
Application Software
  ↓
System Software
  ↓
Hardware

examples:

When you click a file: 
User → File Explorer (Application) → Windows OS (System) → Hard Drive (Hardware)

When you print: 
User → MS Word (Application) → Printer Driver (System) → Printer (Hardware)
```

1. System Software
    - acts as a bridge between hardware and other software

    - eg: OS(Linux, Windows, iOS....), Drivers

2. Application Software

    - Softwares developed to perform specific tasks

    - Types of Application software:

        1. Standalone Applications
            - Eg: Notepad, Calculator, Paint

        2. Mobile Applications
            - Eg: Instagram, WhatsApp, Mobile Games

        3. `Client - Server Applications` 
            
            - Client: User interface (frontend)
            - Server: Business logic and data storage (backend)
            - Requires network connection
            - Eg: 
                - web apps (Gmail, Amazon, YouTube)
                - Cloud Applications (Google Drive)
                - `Django Applications (what we'll build)`

### Client - Server Applications based on architecture

- **2-Tier**
    - 2 layers 
        - Client side (Frontend) + Data Source(eg: Database, file, ....)
    - Example: 
        - An app which takes user input and stores it in a .txt file.
            - Client side: ui with input field
            - storage: .txt file
    - Architecture: [UI] ←→ [Data]

- **3-Tier**
    - 3 layers
        - Client + Server + Data Source(Database)

    - Example: 
        - Modern web apps, 
        - `Django apps`

    - Client side: 
        - Frontend(UI) 
            - technology: React

    - Server side / (Backend):
        - Server:
            - technology: Django
            
        - Data Source(Database)
            - technology: MySQL 

## Three Tier Architecture
![3 Tier architecture](https://www.zirous.com/wp-content/uploads/2022/10/Untitled-5-01.png)