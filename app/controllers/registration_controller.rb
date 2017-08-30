class RegistrationController < ApplicationController
  def index
   @register=Registration.all
  end

  def login
  end

  def logout
  end

def signup
end

  def register
    #byebug;
    user=params[:user];
     name =params[:Name]
     branch =params[:Branch]
     year= params[:Year]
     phone=params[:Phone]
     email=user["Email"]
     team=params[:Team]
     other=params[:Other]

    Registration.create(:Name=>name,:Branch=>branch,:Year=>year,:Phone=>phone,:Email=>email,:Team=>team,:Other=>other);

    return  redirect_to '/index';
  end

end
