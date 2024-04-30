CREATE TABLE Families (
    family_id INT PRIMARY KEY IDENTITY(1,1),
    family_name VARCHAR(100) UNIQUE
);

CREATE TABLE Persons (
    id INT PRIMARY KEY IDENTITY(1,1),
    name VARCHAR(100),
    birth_date DATE,
    photo VARBINARY(MAX),
    father_id INT,
    mother_id INT,
    family_id INT,
    FOREIGN KEY (father_id) REFERENCES Persons(id),
    FOREIGN KEY (mother_id) REFERENCES Persons(id),
    FOREIGN KEY (family_id) REFERENCES Families(family_id)
);