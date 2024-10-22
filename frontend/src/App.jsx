import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate,
} from "react-router-dom";
import { useSelector } from "react-redux";
import Register from "./components/Register.jsx";
import Login from "./components/Login.jsx";
import Profile from "./components/Profile.jsx";

function App() {
  const isAuthenticated = useSelector((state) => state.auth.isAuthenticated);

  return (
    <Router>
      <div className="App">
        <Routes>
          <Route
            path="/register"
            element={
              isAuthenticated ? <Navigate to="/profile" /> : <Register />
            }
          />
          <Route
            path="/login"
            element={isAuthenticated ? <Navigate to="/profile" /> : <Login />}
          />
          <Route
            path="/profile"
            element={isAuthenticated ? <Profile /> : <Navigate to="/login" />}
          />
          <Route
            path="/"
            element={
              isAuthenticated ? (
                <Navigate to="/profile" />
              ) : (
                <Navigate to="/login" />
              )
            }
          />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
