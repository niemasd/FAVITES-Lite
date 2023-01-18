import React, { useState } from "react";
import {
  Button,
  Modal,
  Box,
  Typography,
  Alert,
  IconButton,
  Collapse,
} from "@mui/material";
import { useSelector } from "react-redux";
import styles from "./Header.module.css";


const downloadJson = (config) => {
  const str = JSON.stringify(config);
  const bytes = new TextEncoder().encode(str);
  const blob = new Blob([bytes], {
      type: "application/json;charset=utf-8"
  });
  const href = URL.createObjectURL(blob);
  return href;
}

const Header = (props) => {
  const config = useSelector((state) => state.config.value);
  const [openExport, setOpenExport] = useState(false);
  const [openAlert, setOpenAlert] = useState(false);

  const { className } = props;

  return (
    <div className={`${className} ${styles.Main}`}>
      <h1 className={styles.Title}>
        FAVITES-Lite <span className={styles.AltText}>Config Designer</span>
      </h1>
      <br />
      <Button
        variant="contained"
        onClick={() => {
          console.log(JSON.stringify(config));
          // alert("Config has been printed into the console.");
          setOpenExport(true);
        }}
      >
        Export
      </Button>
      <Modal
        open={openExport}
        onClose={() => {
          setOpenExport(false);
          setOpenAlert(false);
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
            Export Options
          </Typography>
          {/* <Typography id="modal-modal-description" sx={{ mt: 2 }}>
            {JSON.stringify(config)}
          </Typography> */}
          <Button
            variant="contained"
            className={styles.ModalButton}
            onClick={() => {
              navigator.clipboard.writeText(JSON.stringify(config));
              setOpenAlert(true);
            }}
          >
            Copy to Clipboard
          </Button>
          <br />
          <Button
            variant="contained"
            className={styles.ModalButton}
            onClick={() => {
              downloadJson(config);
              setOpenAlert(true);
            }}
          >
            <a href={downloadJson(config)} download="config.json">
              Download JSON File
            </a>
          </Button>
          <br />
          <Collapse in={openAlert}>
            <Alert
              severity="success"
              action={
                <IconButton
                  aria-label="close"
                  color="inherit"
                  size="small"
                  onClick={() => {
                    setOpenAlert(false);
                  }}
                >
                  X
                </IconButton>
              }
              className={styles.ModalAlert}
            >
              Success!
            </Alert>
          </Collapse>

          {/* <Button variant="outlined" className={styles.ModalButton}>
            Export as JSON
          </Button> */}
        </Box>
      </Modal>
    </div>
  );
};

export default Header;
