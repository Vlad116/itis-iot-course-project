
import React from 'react'
import {
    BrowserRouter as Router,
    Switch,
    Route
  } from "react-router-dom";
  import '../App.css'
  import Lighting from './Lighting/index'
  import Ambient from './Ambient/index'
  import About from './About/index'
  import NotFoundPage from './universal-components/NotFoundPage'
  import Navbar from './universal-components/Navbar'
//   import Navbar from './universal-components/Navbar'

const Root = () => {
    return (
        <Router>
            <div className='app'>
            <Navbar />
            <Switch>
                <Route exact path="/" component={Lighting} />
                <Route path='/lighting' header='Lighting' component={Lighting} />
                <Route path='/ambient' header='Ambient' component={Ambient} />
                <Route path='/about' header='About' component={About} />
                <Route component={NotFoundPage} />
            </Switch>
          {/* <Footer /> */}
          </div>
        </Router>
    )
}

export default Root