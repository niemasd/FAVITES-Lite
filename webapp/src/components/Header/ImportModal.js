import React, { useState } from "react";
import {
  Button,
  Modal,
  Box,
  Typography,
  Input,
  TextField,
} from "@mui/material";
import { useDispatch } from "react-redux";
import { setConfig } from "../../features/config/configSlice";
import styles from "./Header.module.css";
import { ErrorAlert, SuccessAlert } from "./Alerts";
import { setSelected } from "../../features/selected/selectedSlice";

const ImportModal = (props) => {
  const [selectedFile, setSelectedFile] = useState();
  const [textboxValue, setTextboxValue] = useState("");
  const [openSuccessAlert, setOpenSuccessAlert] = useState(false);
  const [openErrorAlert, setOpenErrorAlert] = useState(false);
  const dispatch = useDispatch();

  const acceptedFiles = /.json/;

  const uploadHandler = (e) => {
    setSelectedFile(e.target.files[0]);
  };

  const handleSubmission = () => {
    const fileReader = new FileReader();

    if (!selectedFile.type.match(acceptedFiles)) {
      console.log("There is an error with uploading the file");
      return;
    }

    fileReader.onload = (e) => {
      console.log(e.target.result);
      uploadConfig(e.target.result);
    };
    fileReader.readAsText(selectedFile);
  };

  const uploadConfig = (s) => {
    try {
      dispatch(setConfig(JSON.parse(s)));
      setOpenSuccessAlert(true);
    } catch {
      setOpenErrorAlert(true);
    }
  };

  const { open, setOpen } = props;

  return (
    <Modal
      open={open}
      onClose={() => {
        setOpen(false);
        setOpenSuccessAlert(false);
      }}
    >
      <Box
        sx={{
          position: "absolute",
          top: "50%",
          left: "50%",
          transform: "translate(-50%, -50%)",
          width: 400,
          bgcolor: "background.paper",
          border: "2px solid #000",
          boxShadow: 24,
          p: 4,
        }}
      >
        <Typography id="modal-modal-title" variant="h6" component="h2">
          Import Options
        </Typography>
        <br />

        <Input type="file" name="file" onChange={uploadHandler} />
        <br />
        <br />
        <div>
          <Button
            variant="contained"
            className={styles.ModalButton}
            onClick={handleSubmission}
          >
            Use Selected File
          </Button>
        </div>
        <div className={styles.Separator}>OR</div>
        <TextField
          fullWidth
          multiline
          maxRows={4}
          onChange={(e) => {
            setTextboxValue(e.target.value);
          }}
        ></TextField>
        <br />
        <br />
        <div>
          <Button
            variant="contained"
            className={styles.ModalButton}
            onClick={() => {
              uploadConfig(textboxValue);
              dispatch(setSelected("Contact Network"));
            }}
          >
            Use Textbox
          </Button>
        </div>
        <SuccessAlert open={openSuccessAlert} setOpen={setOpenSuccessAlert} />
        <ErrorAlert open={openErrorAlert} setOpen={setOpenErrorAlert} message={"Invalid JSON! Check the JSON string."} />
      </Box>
    </Modal>
  );
};

export default ImportModal;
