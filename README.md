# McDonald's Menu Management

This repository contains a Python script (`McMenu.py`) for managing a McDonald's menu using various functions from `Funciones2.py`.

## Main Program
The script initializes a global variable (`diccMcDonalds`) and reads existing data from the `inventarioMc` file. It then calls the `menu` function to start the main menu loop.

## Function Details:

### 1. `menu`
   - **Description:**
     The main menu function allows the user to add, modify, search, or delete food items from the McDonald's menu. It also provides an option to exit the program.

### 2. `menuSecundario`
   - **Description:**
     A secondary menu function that offers options to display all registered foods or search for a food item by its code.

### 3. `lee`
   - **Description:**
     Reads data from a file (`inventarioMc`) and returns a dictionary.

### 4. `grabar`
   - **Description:**
     Writes data to a file (`inventarioMc`).

### 5. `agregarComida`
   - **Description:**
     Allows the user to add a new food item to the menu. It prompts the user for information such as code, name, price, and ingredients.

### 6. `modificarComida`
   - **Description:**
     Allows the user to modify an existing food item by providing its code.

### 7. `mostrarTodasComidas`
   - **Description:**
     Displays details of all registered food items.

### 8. `mostrarComida`
   - **Description:**
     Displays details of a specific food item based on its code.

### 9. `eliminarComida`
   - **Description:**
     Deletes a food item from the menu based on its code.
