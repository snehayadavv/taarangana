Rails.application.routes.draw do

  get '/' => 'registration#signup'
  get '/login' => 'registration#login'

  get '/logout' =>'registration#logout'
  get '/index'=>'registration#index'
  post '/register' => 'registration#register'



  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
