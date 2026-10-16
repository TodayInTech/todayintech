import React, {useEffect, useId, useRef, useState} from 'react';
import {createPortal} from 'react-dom';
import styles from './styles.module.css';

export default function Tooltip({content, label}) {
  const id = useId();
  const trigger = useRef(null);
  const [position, setPosition] = useState(null);
  const close = () => setPosition(null);
  const show = () => {
    const rect = trigger.current.getBoundingClientRect();
    setPosition({left: Math.max(142, Math.min(window.innerWidth - 142, rect.left + rect.width / 2)), top: rect.bottom + 5});
  };
  useEffect(() => {
    if (!position) return undefined;
    const escape = (event) => { if (event.key === 'Escape') close(); };
    const outside = (event) => { if (!trigger.current?.contains(event.target)) close(); };
    window.addEventListener('pointerdown', outside);
    window.addEventListener('keydown', escape);
    window.addEventListener('scroll', close, true);
    window.addEventListener('resize', close);
    return () => {
      window.removeEventListener('pointerdown', outside);
      window.removeEventListener('keydown', escape);
      window.removeEventListener('scroll', close, true);
      window.removeEventListener('resize', close);
    };
  }, [position]);
  return <span className={styles.root} onMouseEnter={show} onMouseLeave={close}>
    <button ref={trigger} type="button" className={styles.trigger} aria-label={label}
      aria-describedby={position ? id : undefined} onFocus={show} onBlur={close}
      onClick={show}>i</button>
    {position && createPortal(<span id={id} role="tooltip" className={styles.content} style={position}>{content}</span>, document.body)}
  </span>;
}
