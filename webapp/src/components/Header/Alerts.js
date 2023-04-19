import React from "react";
import { Alert, IconButton, Collapse } from "@mui/material";
import styles from "./Header.module.css";

export const SuccessAlert = (props) => {
  const { open, setOpen } = props;

  return (
    <Collapse in={open}>
      <Alert
        severity="success"
        action={
          <IconButton
            aria-label="close"
            color="inherit"
            size="small"
            onClick={() => {
              setOpen(false);
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
  );
};

export const ErrorAlert = (props) => {
    const { open, setOpen, message } = props;

  return (
    <Collapse in={open}>
      <Alert
        severity="error"
        action={
          <IconButton
            aria-label="close"
            color="inherit"
            size="small"
            onClick={() => {
              setOpen(false);
            }}
          >
            X
          </IconButton>
        }
        className={styles.ModalAlert}
      >
        Error! {message}
      </Alert>
    </Collapse>
  );
}