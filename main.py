import mysql.connector
from drones import Drone, DroneStore

class Application(object):
    """ Main application wrapper for processing input. """

    def __init__(self, conn):
        self._drones = DroneStore(conn)
        self._commands = {
            'list': self.list,
            'add': self.add,
            'update': self.update,
            'remove': self.remove,
            'allocate': self.allocate,
            'help': self.help,
        }

    def main_loop(self):
        print('Welcome to DALSys')
        cont = True
        while cont:
            val = input('> ').strip()
            cmd = None
            args = {}
            if len(val) == 0:
                continue

            try:
                parts = val.split(' ')
                parts[0] = parts[0].lower()
                if parts[0] == 'quit':
                    cont = False
                    print('Exiting DALSys')
                else:
                    cmd = self._commands[parts[0]]
            except KeyError:
                print('!! Unknown command "%s" !!' % (val))

            if cmd is not None:
                args = parts[1:]
                try:
                    cmd(args)
                except Exception as ex:
                    print('!! %s !!' % (str(ex)))

    def add(self, args):
        """ Adds a new drone. """
        if len(args) == 0:
            raise Exception("Name is required!")
        new_arg = []
        string_name = ""
        counter = 0
        quote_mark = 0
        
        if (len(args) != 2 and "-rescue" not in args) or (len(args) != 3 and "-rescue" in args):
            while counter < len(args):
                if "'" in args[counter] or '"' in args[counter]:
                    quote_mark += 1
                if quote_mark == 1:
                    string_name = string_name + args[counter] + " "
                if quote_mark == 2:
                    string_name = string_name + args[counter]
                    for i in range(0, counter+1):
                        args.pop(0)
                    break
                counter += 1
            new_arg.append(string_name)
            new_arg = new_arg + args
            args = new_arg
        
        if len(args) == 1:
            raise Exception("Class type is required")
        for argument in args:
            if "class" in argument:
                if int(argument[-1]) == 1:
                    args[1] = 1
                elif int(argument[-1]) == 2:
                    args[1] = 2
                else:
                    raise Exception("Unknown drone class or incorrect command")
        
        if "-rescue" in args:
            name = args[0]
            a_drone = Drone(name, args[1], True)
        else:
            name = args[0]
            a_drone = Drone(name, args[1])
        a_drone.name = a_drone.name.strip("'\"")
        
        query = "INSERT INTO drone_table(name, class_type, rescue_type) \
        VALUES('" + str(a_drone.name) + "', " + str(a_drone.class_type) + ", " + str(a_drone.rescue) + ");"
        dbcursor = conn.cursor(buffered=True)
        dbcursor.execute(query)
        print("Added rescue drone with " + str(a_drone.name))
        
        dbcursor.close()    
        #raise Exception("Add method has not been implemented yet")

    def allocate(self, args):
        """ Allocates a drone to an operator. """
        raise Exception("Allocate method has not been implemented yet")

    def help(self, args):
        """ Displays help information. """
        print("Valid commands are:")
        print("* list [- class =(1|2)] [- rescue ]")
        print("* add 'name ' -class =(1|2) [- rescue ]")
        print("* update id [- name ='name '] [- class =(1|2)] [- rescue ]")
        print("* remove id")
        print("* allocate id 'operator'")

    def list(self, args):
        """ Lists all the drones in the system. """
        query = "SELECT drone_table.*, CONCAT(operator_table.first_name, ' ', operator_table.last_name) \
        FROM drone_table LEFT JOIN operator_table ON drone_table.operator_ID = operator_table.ID"
        if "-rescue" in args:
            query += " WHERE rescue_type = TRUE"
        for argument in args:
            if "class" in argument:
                if int(argument[-1]) == 1:
                    if "-rescue" in args:
                        query += " AND class_type = 1"
                    else:
                        query += " WHERE class_type = 1"
                elif int(argument[-1]) == 2:
                    if "-rescue" in args:
                        query += " AND class_type = 2"
                    else:
                        query += " WHERE class_type = 1"
                else:
                    raise Exception("Unknown drone class " + argument[-1])
        query += ";"
        
        dbcursor = conn.cursor(buffered=True)
        dbcursor.execute(query)
        
        count = 0
        formatted = []
        for entry in dbcursor:
            show = list(entry)
            if entry[5] == None:
                show[5] = "<none>"
            if entry[3] == 0:
                show[3] = "No"
            else:
                show[3] = "Yes"
            if entry[2] == 1:
                show[2] = "One"
            elif entry[2] == 2:
                show[2] = "Two"
            formatted.append(show)
            count += 1
        if count == 0:
            raise Exception("There are no drones for this criteria")
        else:
            print("{:4}".format("ID"), "{:20}".format("Name"), "{:7}".format("Class"), "{:8}".format("Rescue"), "{:14}".format("Operator"))
            for entry in formatted:
                print("{0:0>4}".format(str(entry[0])), "{:20}".format(str(entry[1])), "{:7}".format(str(entry[2])), "{:8}".format(str(entry[3])), 
                  "{:14}".format(str(entry[5])))
            print(str(count) + " drones listed")
        dbcursor.close()
        #raise Exception("List method has not been implemented yet")

    def remove(self, args):
        """ Removes a drone. """
        if len(args) == 0:
            raise Exception("ID is required")
        else:
            query = "SELECT * FROM drone_table WHERE ID = " + str(args[0]) + ";"
            dbcursor = conn.cursor(buffered=True)
            dbcursor.execute(query)
            count = 0
            for entry in dbcursor:
                count += 1
            if count == 0:
                raise Exception("Unknown drone")
            dbcursor.close()
            
            query = "DELETE FROM drone_table WHERE ID = " + str(args[0]) + ";"
            dbcursor = conn.cursor(buffered=True)
            dbcursor.execute(query)
            print("Drone removed")
            dbcursor.close()
        #raise Exception("Remove method has not been implemented yet")

    def update(self, args):
        """ Updates the details for a drone. """
        
        raise Exception("Update method has not been implemented yet")


if __name__ == '__main__':
    conn = mysql.connector.connect(user='wany889',
                                   password='13fe7c42',
                                   host='studdb-mysql.fos.auckland.ac.nz',
                                   database='stu_wany889_COMPSCI_280_C_S2_2019',
                                   charset = "utf8")
    app = Application(conn)
    app.main_loop()
    conn.close()
