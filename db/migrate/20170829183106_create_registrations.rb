class CreateRegistrations < ActiveRecord::Migration[5.1]
  def change
    create_table :registrations do |t|
      t.string :Name
      t.string :Branch
      t.integer :Year
      t.integer :Phone
      t.string :Email
      t.string :Team
      t.text :Other

      t.timestamps
    end
  end
end
