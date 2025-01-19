import React, { useState } from "react";
import {
  Form,
  FormGroup,
  Label,
  Input,
  Button,
  Modal,
  ModalHeader,
  ModalBody,
  ModalFooter,
} from "reactstrap";
import { FaInfoCircle } from "react-icons/fa";

const UserForm = ({ onSubmit }) => {
  const [modal, setModal] = useState(false);
  const [themes, setThemes] = useState([]);
  const [themeInput, setThemeInput] = useState("");

  const toggleModal = () => setModal(!modal);

  const handleSubmit = (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = {
      language: formData.get("language"),
      level: formData.get("level"),
      themes: themes,
    };
    onSubmit(data);
  };

  const handleThemeChange = (event) => {
    setThemeInput(event.target.value);
  };

  const handleAddTheme = () => {
    if (themeInput.trim()) {
      setThemes([...themes, themeInput.trim()]);
      setThemeInput("");
    }
  };

  const handleRemoveTheme = (index) => {
    setThemes(themes.filter((_, i) => i !== index));
  };

  return (
    <>
      <Form
        onSubmit={handleSubmit}
        style={{ paddingTop: "20px", maxWidth: "400px", margin: "0 auto" }}
      >
                <FormGroup>
          <Label for="language">What is your native language?</Label>
          <Input
            type="select"
            name="language"
            id="language"
            required
            style={{ width: "400px" }}
          >
            <option value="">Select a language</option>
            <option value="English">English</option>
            <option value="Spanish">Spanish</option>
            <option value="French">French</option>
            <option value="German">German</option>
            <option value="Chinese">Chinese</option>
          </Input>
        </FormGroup>
        <FormGroup>
          <Label for="language">What language would you like to learn?</Label>
          <Input
            type="select"
            name="language"
            id="language"
            required
            style={{ width: "400px" }}
          >
            <option value="">Select a language</option>
            <option value="English">English</option>
            <option value="Spanish">Spanish</option>
            <option value="French">French</option>
            <option value="German">German</option>
            <option value="Chinese">Chinese</option>
          </Input>
        </FormGroup>
        <FormGroup>
          <Label for="level">
            What is your level in this language?{" "}
            <FaInfoCircle onClick={toggleModal} style={{ cursor: "pointer" }} />
          </Label>
          <Input
            type="select"
            name="level"
            id="level"
            required
            style={{ width: "400px" }}
          >
            <option value="">Select your level</option>
            <option value="NA">I don't know</option>
            <option value="A1">A1</option>
            <option value="A2">A2</option>
            <option value="B1">B1</option>
            <option value="B2">B2</option>
            <option value="C1">C1</option>
          </Input>
        </FormGroup>
        <FormGroup>
          <Label for="themes">What themes interest you?</Label>
          <Input
            type="text"
            name="themes"
            id="themes"
            placeholder="Enter a theme and press Add"
            value={themeInput}
            onChange={handleThemeChange}
            style={{ width: "400px" }}
          />
          <Button
            type="button"
            onClick={handleAddTheme}
            style={{ marginTop: "10px" }}
          >
            Add Theme
          </Button>
          <div style={{ marginTop: "10px" }}>
            {themes.map((theme, index) => (
              <Button
                key={index}
                color="primary"
                outline
                style={{ marginRight: "5px", marginBottom: "5px" }}
                onClick={() => handleRemoveTheme(index)}
              >
                {theme} <span style={{ marginLeft: "5px" }}>x</span>
              </Button>
            ))}
          </div>
        </FormGroup>
        <Button type="submit">Submit</Button>
      </Form>

      <Modal isOpen={modal} toggle={toggleModal}>
        <ModalHeader toggle={toggleModal}>Language Levels</ModalHeader>
        <ModalBody>
          <p>
            <strong>A1:</strong> Beginner
          </p>
          <p>
            <strong>A2:</strong> Elementary
          </p>
          <p>
            <strong>B1:</strong> Intermediate
          </p>
          <p>
            <strong>B2:</strong> Upper Intermediate
          </p>
          <p>
            <strong>C1:</strong> Advanced
          </p>
        </ModalBody>
        <ModalFooter>
          <Button color="secondary" onClick={toggleModal}>
            Close
          </Button>
        </ModalFooter>
      </Modal>
    </>
  );
};

export default UserForm;
