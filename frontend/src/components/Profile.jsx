import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import apiClient from "../utils/apiHelper";
import { logout, setUser } from "../redux/slices/authSlice";

const Profile = () => {
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const user = useSelector((state) => state.auth.user);

  useEffect(() => {
    const fetchUser = async () => {
      try {
        const response = await apiClient.get("/users/me");
        dispatch(setUser(response.data));
      } catch (error) {
        console.error("Failed to fetch user:", error);
        dispatch(logout());
        navigate("/login");
      }
    };

    if (!user) {
      fetchUser();
    }
  }, [user, dispatch, navigate]);

  const handleLogout = () => {
    dispatch(logout());
    navigate("/login");
  };

  if (!user) return <div>Loading...</div>;

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-md w-full space-y-8">
        <h2 className="mt-6 text-center text-3xl font-extrabold text-gray-900">
          Profile
        </h2>
        <div className="mt-8 space-y-6">
          <p className="text-center text-lg">Welcome, {user.username}!</p>
          <p className="text-center">Email: {user.email}</p>
          <button
            onClick={handleLogout}
            className="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          >
            Logout
          </button>
        </div>
      </div>
    </div>
  );
};

export default Profile;
