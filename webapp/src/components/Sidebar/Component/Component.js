import styles from "./Component.module.css";

const Component = (props) => {
  const { name, onClick, className } = props;

  return (
    <div className={`${className} ${styles.Main}`} onClick={onClick}>
      <h4>{name}</h4>
      <span>Not Selected</span>
    </div>
  );
};

export default Component;
