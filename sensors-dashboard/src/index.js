import React from 'react';
import { render } from 'react-dom';
import { Root as App } from './components/Root';
import { AppContainer } from 'react-hot-loader'
import './index.css';
import reportWebVitals from './reportWebVitals';

const rootElement = document.getElementById('root')

render(
  <AppContainer>
      <App />
  </AppContainer>,
  rootElement
)

if (module.hot) {
  module.hot.accept('./components/Root', () => {
      const NewRoot = require('./components/Root').default
      render(
          <AppContainer>
              <NewRoot />
          </AppContainer>,
          rootElement
      )
  })
}

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
