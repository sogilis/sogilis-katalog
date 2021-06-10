#[cfg(test)]
#[path = "./cartesian_test.rs"]
mod cartesian_test;

fn main() {
    let args: Vec<String> = std::env::args().collect();
    if args.len() != 2 {
        return;
    }
    let input = args.get(1).unwrap();

    let message = cartesian_decoder(input);
    println!("\n{}", message);

}

fn cartesian_decoder(input: &String) -> String {
    input.to_string()
}

