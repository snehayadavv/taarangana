require 'test_helper'

class RegistrationControllerTest < ActionDispatch::IntegrationTest
  test "should get index" do
    get registration_index_url
    assert_response :success
  end

  test "should get login" do
    get registration_login_url
    assert_response :success
  end

  test "should get logout" do
    get registration_logout_url
    assert_response :success
  end

end
