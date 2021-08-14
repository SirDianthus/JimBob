# Manual imports
from future import with_statement

# Self Imports

def reload_me():
  os.execv(sys.argv[0]. sys.argv)

def write_class(class_object: class2write):
  # TODO: process the class structure provided and write to a new class file
  with open("classes/"+class2write+".py", "a") as c:
    c.write("class " + class2write.name + ":\n")
    foreach class2write.attributes as attrib:
      c.write(attrib + "\n")
  append_methods(class2write)
  # TODO: verify that the add import works as expected.
  with open(__file__, "r+") as f:
    for i, line in enumerate(f):
      if line == "# Self Imports":
        f.seek(i+1)
        f.write("import " + class2write.name + "\n")
  reload_me()

def append_methods(class_object: class2write):
  # TODO: process the method object passed and write the appropriate class file
  with open("classes/"+class2write.name+".py", "a") as c:
    foreach class2write.methods as method:
      c.write("def " + method.name + ":\n")
      foreach method.body as line:
        c.write("  " + line)
  reload_me()

# Main application loop where the app will prompt you for commands to run.
# If no command can be found to run will prompt for teaching how to run the command.
# should probably use regex to identify the classes/methods to run
# for example ^[open|start|run] should map to an exec. http[s]://[a-z].[a-z]{2-4} should map to opening the url
def __main__():
  # TODO: main application loop
  command = input("Hello Sir, what can i help you with today? >")
  if command in exec("dir()"):
    exec(command)
  else:
    prompt_for_learn()
  while true:
    command = input("Anything else Sir? > ")
    if command in exec("dir()"):
      exec(command)
    else:
      prompt_for_learn()

def prompt_for_learn:
  if (input("Sorry Sir, I don't know how to do that yet, do you have time to teach me?") == "sure"):
      new_class = class_object(input("What should I call the new class? "))
      attribute_list = input("What attributes should it have? (preferably in a comma seperated list) ")
      foreach attribute_list.split(", ") as attribute:
        new_class.add_attribute(attribute)
      while (input("Do You want to add a method? ") == "yeah"):
        new_method = method_object(input("What is the name of the method? "))
        while (input("Do You have another line to add to the body? ") == "yes"):
          new_method.add_body_line("  " + input("> "))

class class_object:
  name = generic
  attributes = []
  methods = []

  def __init__(self, name):
    self.name = name

  def add_attribute(self, attribute):
    self.attributes.append(attribute)

  # method_body is an array of strings, one per line.
  def add_method(self, method_name, method_body):
    self.methods.append(method_object(method_name, method_body))

class method_object:
  name = "generic method"
  body = []

  def __init__(self, name):
    self.name = name
  def add_body_line(self, line):
    self.body.append(line)