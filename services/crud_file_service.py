class FileService:

    def create_file(self, name):
        file = open(name, "w+")
        return file

    def load_file(self, name):
        # Creates The File with the function create file
        file = self.create_file('test_file.txt')
        # Add Content to the file
        for i in range(10):
            file.write("This is line %d\r" % (i + 1))
        # Close the file
        file.close()
        # Return the file with the new registers
        return file

    def read_file(self, name, key):
        # Open the file in order to read the lines
        with open(name) as file:
            for line in file:
                if line == key:
                    return True
        # Close the file
        file.close()
        return file
