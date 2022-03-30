require "spec_helper"

describe SampleClass do
  subject { SampleClass.new }
  it "should work" do
    expect(subject.foo).to eq("bar")
  end
end
