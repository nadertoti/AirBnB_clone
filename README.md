# HBNB Command Interpreter

This is a simple command interpreter for the HBNB project.

## Installation

To install, simply clone the repository:

```
git clone https://github.com/holberton-school/hbnb_console.git
```

## Usage

To start the interpreter, simply run the following command:

```
python3 console.py
```

The interpreter will then prompt you for input. You can enter any of the following commands:

* `create`: Create a new instance of a class.
* `show`: Show the details of an instance.
* `destroy`: Delete an instance.
* `all`: List all instances of a class.
* `update`: Update the attributes of an instance.
* `quit`: Quit the interpreter.

## Examples

Here are some examples of how to use the interpreter:

```
# Create a new instance of the BaseModel class
create BaseModel

# Show the details of the instance
show BaseModel <instance_id>

# Destroy the instance
destroy BaseModel <instance_id>

# List all instances of the BaseModel class
all BaseModel

# Update the attributes of an instance
update BaseModel <instance_id> name <new_name>
```

## Contributing

Contributions are welcome! Please read the [contributing guidelines](https://github.com/holberton-school/hbnb_console/blob/master/CONTRIBUTING.md) before submitting a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/holberton-school/hbnb_console/blob/master/LICENSE) file for details.